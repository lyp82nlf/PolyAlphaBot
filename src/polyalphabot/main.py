from __future__ import annotations

import argparse
import logging
import os
import time
from urllib.request import Request
from urllib.error import HTTPError
from queue import Queue

from polyalphabot.config.settings import SettingsLoader
from polyalphabot.core.engine import EngineConfig, TradingEngine
from polyalphabot.core.risk import RiskManager
from polyalphabot.execution.executor import Executor
from polyalphabot.strategies.tge_market_sweep import TgeMarketSweepStrategy
from polyalphabot.adapters.factory import build_adapters
from polyalphabot.services.notification import WeComConfig, WeComNotifier
from polyalphabot.services.consumer import MarketConsumer
from polyalphabot.services.polymarket_gamma import GammaClient, GammaConfig
from polyalphabot.services.polymarket_market_store import PolymarketStore
from polyalphabot.services.polymarket_market_watcher import MarketWatcherConfig, PolymarketMarketWatcher
from polyalphabot.services.tge_factory import build_sources
from polyalphabot.services.tge_deduper import TgeDeduper
from polyalphabot.services.tge_store import TgeStore
from polyalphabot.services.tge_runner import TgeProducer, TgeEnvelope
from polyalphabot.utils.logging import setup_logging
from polyalphabot.utils.http import resolve_proxies, urlopen_with_proxy


def build_engines(settings, notifier, proxies) -> list[TradingEngine]:
    adapter_configs = settings.adapters or [settings.adapter]
    adapters = build_adapters(adapter_configs, notifier=notifier, proxies=proxies)
    engines: list[TradingEngine] = []
    for adapter in adapters:
        strategy = TgeMarketSweepStrategy(settings.strategy)
        risk = RiskManager(settings.risk)
        executor = Executor(adapter)
        engines.append(
            TradingEngine(
                adapter=adapter,
                strategy=strategy,
                risk_manager=risk,
                executor=executor,
                config=settings.engine,
            )
        )
    return engines


def _mask_proxy(proxy_value: str | None) -> str:
    if not proxy_value:
        return "none"
    if "://" not in proxy_value:
        return proxy_value
    scheme, rest = proxy_value.split("://", 1)
    if "@" not in rest:
        return f"{scheme}://{rest}"
    creds, host = rest.split("@", 1)
    if ":" in creds:
        return f"{scheme}://***:***@{host}"
    return f"{scheme}://***@{host}"


def _check_market_proxy(notifier: WeComNotifier, proxies: dict[str, str] | None) -> None:
    if not proxies:
        logging.info("Market proxy not configured.")
        return
    masked = {k: _mask_proxy(v) for k, v in proxies.items()}
    logging.info("Market proxy configured: %s", masked)
    endpoints = [
        (
            "gamma",
            "https://gamma-api.polymarket.com/public-search?q=launch%20a%20token&page=1&limit_per_type=1",
            {"accept": "application/json", "user-agent": "Mozilla/5.0"},
        ),
        (
            "clob",
            "https://clob.polymarket.com/health",
            {"accept": "application/json", "user-agent": "Mozilla/5.0"},
        ),
    ]
    for name, url, headers in endpoints:
        request = Request(url, headers=headers)
        try:
            with urlopen_with_proxy(request, timeout=5, proxies=proxies) as response:
                response.read(256)
            logging.info("Market proxy check ok: %s", name)
        except HTTPError as exc:
            if exc.code in (401, 403, 404, 405):
                logging.info("Market proxy check ok (http %s): %s", exc.code, name)
                continue
            logging.warning("Market proxy check failed: %s err=%s", name, exc)
            notifier.send_markdown(
                "市场代理检测失败",
                f"**endpoint**: <font color=\"warning\">{name}</font>\n"
                f"**error**: <font color=\"warning\">{exc}</font>",
            )
        except Exception as exc:
            logging.warning("Market proxy check failed: %s err=%s", name, exc)
            notifier.send_markdown(
                "市场代理检测失败",
                f"**endpoint**: <font color=\"warning\">{name}</font>\n"
                f"**error**: <font color=\"warning\">{exc}</font>",
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--directory")
    args = parser.parse_args()

    settings = SettingsLoader.load(args.config)
    setup_logging(logging.INFO, log_path=settings.log_path)
    if args.directory:
        try:
            os.chdir(args.directory)
        except OSError as exc:
            logging.error("Failed to change directory to %s: %s", args.directory, exc)
            raise
    market_proxies = resolve_proxies(
        http_proxy=settings.http_proxy,
        https_proxy=settings.https_proxy,
        all_proxy=settings.all_proxy,
    )
    no_proxy: dict[str, str] = {}
    sources = build_sources(settings.tge_sources, proxies=no_proxy)
    notifier = WeComNotifier(
        WeComConfig(
            webhook_url=settings.wecom_webhook_url,
            cooldown_seconds=settings.wecom_cooldown_seconds,
            proxies=no_proxy,
        )
    )
    _check_market_proxy(notifier, market_proxies)
    engines = build_engines(settings, notifier, market_proxies)
    consumer = MarketConsumer(engines, settings.consumer_max_workers, notifier)

    gamma = GammaClient(
        GammaConfig(
            headers=settings.gamma_headers,
            timeout_seconds=settings.gamma_timeout_seconds,
            retries=settings.gamma_retries,
            retry_backoff_seconds=settings.gamma_retry_backoff_seconds,
            proxies=market_proxies,
        )
    )
    store = PolymarketStore(settings.market_db_path)
    watcher = PolymarketMarketWatcher(
        gamma=gamma,
        store=store,
        notifier=notifier,
        config=MarketWatcherConfig(
            poll_interval_seconds=settings.market_poll_interval_seconds,
            query="launch a token",
            error_threshold=settings.market_error_threshold,
            error_window_seconds=settings.market_error_window_seconds,
            error_cooldown_seconds=settings.market_error_cooldown_seconds,
        ),
    )
    watcher.start()
    logging.info("Market watcher started: interval=%ss", settings.market_poll_interval_seconds)

    queue: Queue[TgeEnvelope] = Queue()
    tge_store = TgeStore(settings.tge_db_path)
    deduper = TgeDeduper(window_seconds=settings.dedup_window_seconds, store=tge_store)
    for source in sources:
        producer = TgeProducer(
            source=source,
            out_queue=queue,
            poll_interval_seconds=settings.poll_interval_seconds,
            notifier=notifier,
            error_threshold=settings.error_threshold,
            error_window_seconds=settings.error_window_seconds,
            deduper=deduper,
        )
        producer.start()
        logging.info("TGE source started: %s interval=%ss", source.name(), settings.poll_interval_seconds)

    while True:
        try:
            envelope = queue.get(timeout=5)
        except Exception:
            logging.info("Main loop idle: waiting for TGE signals.")
            continue
        logging.info(
            "TGE signal received from %s: %s %s",
            envelope.source,
            envelope.signal.token_symbol,
            envelope.signal.token_name,
        )
        consumer.submit(envelope.signal)


if __name__ == "__main__":
    main()
