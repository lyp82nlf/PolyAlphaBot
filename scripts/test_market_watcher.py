from __future__ import annotations

import logging
from pathlib import Path

from polyalphabot.config.settings import SettingsLoader
from polyalphabot.services.notification import WeComConfig, WeComNotifier
from polyalphabot.services.polymarket_gamma import GammaClient, GammaConfig
from polyalphabot.services.polymarket_market_store import PolymarketStore
from polyalphabot.services.polymarket_market_watcher import MarketWatcherConfig, PolymarketMarketWatcher


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s")
    settings = SettingsLoader.load("config.json")

    test_db = Path("data/test_markets.db")
    if test_db.exists():
        test_db.unlink()

    logging.info(
        "WeCom webhook configured=%s",
        "yes" if settings.wecom_webhook_url else "no",
    )
    gamma = GammaClient(GammaConfig(headers=settings.gamma_headers, timeout_seconds=10))
    store = PolymarketStore(test_db)
    notifier = WeComNotifier(
        config=WeComConfig(
            webhook_url=settings.wecom_webhook_url,
            timeout_seconds=10,
            cooldown_seconds=0,
        )
    )
    watcher = PolymarketMarketWatcher(
        gamma=gamma,
        store=store,
        notifier=notifier,
        config=MarketWatcherConfig(
            poll_interval_seconds=60,
            query="launch a token",
            limit_per_type=5,
            keep_closed_markets=1,
        ),
    )

    logging.info("Starting market watcher test.")
    try:
        events, markets = watcher._fetch_all()
        logging.info("Fetched events=%s markets=%s", len(events), len(markets))
        new_events = store.upsert_events(events)
        store.upsert_markets(markets)
        logging.info("New events=%s", len(new_events))
        if new_events:
            watcher._notify_new_events(new_events)
            logging.info("WeCom notification sent.")
        else:
            logging.info("No new events to notify.")
    finally:
        logging.info("Market watcher test finished.")


if __name__ == "__main__":
    main()
