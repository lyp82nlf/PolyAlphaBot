from __future__ import annotations

import argparse
import logging
import os
import time
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
from polyalphabot.utils.http import resolve_proxies


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
    proxies = resolve_proxies(
        http_proxy=settings.http_proxy,
        https_proxy=settings.https_proxy,
        all_proxy=settings.all_proxy,
    )
    sources = build_sources(settings.tge_sources, proxies=proxies)
    notifier = WeComNotifier(
        WeComConfig(
            webhook_url=settings.wecom_webhook_url,
            cooldown_seconds=settings.wecom_cooldown_seconds,
            proxies=proxies,
        )
    )
    engines = build_engines(settings, notifier, proxies)
    consumer = MarketConsumer(engines, settings.consumer_max_workers, notifier)

    gamma = GammaClient(
        GammaConfig(
            headers=settings.gamma_headers,
            timeout_seconds=settings.gamma_timeout_seconds,
            retries=settings.gamma_retries,
            retry_backoff_seconds=settings.gamma_retry_backoff_seconds,
            proxies=proxies,
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
