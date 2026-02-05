from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class TgeRecord:
    source: str
    token_symbol: str
    token_name: str
    launch_time: str | None
    received_at: str
    raw_json: str


class TgeStore:
    def __init__(self, path: str | Path) -> None:
        self._path = Path(path)
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(self._path, check_same_thread=False)
        self._conn.execute("PRAGMA journal_mode=WAL;")
        self._conn.execute("PRAGMA synchronous=NORMAL;")
        self._init_schema()

    def _init_schema(self) -> None:
        self._conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tge_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT,
                token_symbol TEXT,
                token_name TEXT,
                launch_time TEXT,
                received_at TEXT,
                raw_json TEXT
            )
            """
        )
        self._conn.execute(
            """
            CREATE UNIQUE INDEX IF NOT EXISTS idx_tge_unique
            ON tge_events(token_symbol, token_name, launch_time)
            """
        )
        self._conn.commit()

    def insert_if_new(self, record: TgeRecord) -> bool:
        cursor = self._conn.execute(
            """
            SELECT 1
            FROM tge_events
            WHERE token_symbol = ? COLLATE NOCASE
              AND token_name = ? COLLATE NOCASE
            LIMIT 1
            """,
            (record.token_symbol, record.token_name),
        )
        if cursor.fetchone():
            return False
        try:
            self._conn.execute(
                """
                INSERT INTO tge_events (source, token_symbol, token_name, launch_time, received_at, raw_json)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    record.source,
                    record.token_symbol,
                    record.token_name,
                    record.launch_time,
                    record.received_at,
                    record.raw_json,
                ),
            )
            self._conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def close(self) -> None:
        self._conn.close()
