from __future__ import annotations

import json
import logging
from polyalphabot.config.settings import SettingsLoader
from polyalphabot.services.polymarket_clob import ClobClient, ClobConfig

TOKENS = [
    "67841192750148997275473648690260112080723046610172086481620702839701751895916",
    "99198924097827784427532997585241286678466293148323233780401857923587127415754",
]


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    settings = SettingsLoader.load("config.json")
    clob_headers = (
        settings.adapters[0].extra.get("clob_headers")
        if settings.adapters
        else {}
    )
    clob_timeout = (
        int(settings.adapters[0].extra.get("clob_timeout_seconds", 20))
        if settings.adapters
        else 20
    )
    client = ClobClient(ClobConfig(headers=clob_headers, timeout_seconds=clob_timeout))

    req = [{"token_id": t, "side": "BUY"} for t in TOKENS]
    logging.info("Requesting order books: count=%s", len(req))
    books = client.get_books(req)
    if not books:
        logging.warning("Empty response from CLOB /books")
    print(json.dumps(books, indent=2))


if __name__ == "__main__":
    main()
