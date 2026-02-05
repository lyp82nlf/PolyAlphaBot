from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List

from polyalphabot.services.threading_utils import make_lock


@dataclass(frozen=True)
class EventRecord:
    event_id: str
    title: str
    slug: str
    created_at: str | None
    updated_at: str | None
    event_date: str | None
    raw_json: str


@dataclass(frozen=True)
class MarketRecord:
    market_id: str
    event_id: str
    question: str
    slug: str
    active: bool
    closed: bool
    event_date: str | None
    raw_json: str


class PolymarketStore:
    def __init__(self, path: str | Path) -> None:
        self._path = Path(path)
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(self._path, check_same_thread=False)
        self._lock = make_lock()
        self._conn.execute("PRAGMA journal_mode=WAL;")
        self._conn.execute("PRAGMA synchronous=NORMAL;")
        self._init_schema()

    def _init_schema(self) -> None:
        with self._lock:
            self._conn.execute(
                """
                CREATE TABLE IF NOT EXISTS events (
                    event_id TEXT PRIMARY KEY,
                    title TEXT,
                    slug TEXT,
                    created_at TEXT,
                    updated_at TEXT,
                    event_date TEXT,
                    raw_json TEXT
                )
                """
            )
            self._conn.execute(
                """
                CREATE TABLE IF NOT EXISTS markets (
                    market_id TEXT PRIMARY KEY,
                    event_id TEXT,
                    question TEXT,
                    slug TEXT,
                    active INTEGER,
                    closed INTEGER,
                    event_date TEXT,
                    raw_json TEXT
                )
                """
            )
            self._add_column_if_missing("events", "event_date", "TEXT")
            self._add_column_if_missing("markets", "event_date", "TEXT")
            self._conn.execute(
                """
                CREATE INDEX IF NOT EXISTS idx_markets_question
                ON markets(question)
                """
            )
            self._conn.execute(
                """
                CREATE INDEX IF NOT EXISTS idx_markets_slug
                ON markets(slug)
                """
            )
            self._conn.commit()

    def _add_column_if_missing(self, table: str, column: str, col_type: str) -> None:
        cur = self._conn.execute(f"PRAGMA table_info({table})")
        existing = {row[1] for row in cur.fetchall()}
        if column in existing:
            return
        self._conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} {col_type}")

    def upsert_events(self, events: Iterable[EventRecord]) -> List[EventRecord]:
        new_events: List[EventRecord] = []
        with self._lock:
            for event in events:
                cur = self._conn.execute("SELECT 1 FROM events WHERE event_id = ?", (event.event_id,))
                if cur.fetchone() is None:
                    new_events.append(event)
                self._conn.execute(
                    """
                    INSERT INTO events (event_id, title, slug, created_at, updated_at, event_date, raw_json)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(event_id) DO UPDATE SET
                        title=excluded.title,
                        slug=excluded.slug,
                        created_at=excluded.created_at,
                        updated_at=excluded.updated_at,
                        event_date=excluded.event_date,
                        raw_json=excluded.raw_json
                    """,
                    (
                        event.event_id,
                        event.title,
                        event.slug,
                        event.created_at,
                        event.updated_at,
                        event.event_date,
                        event.raw_json,
                    ),
                )
            self._conn.commit()
        return new_events

    def upsert_markets(self, markets: Iterable[MarketRecord]) -> None:
        with self._lock:
            for market in markets:
                self._conn.execute(
                    """
                    INSERT INTO markets (market_id, event_id, question, slug, active, closed, event_date, raw_json)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(market_id) DO UPDATE SET
                        event_id=excluded.event_id,
                        question=excluded.question,
                        slug=excluded.slug,
                        active=excluded.active,
                        closed=excluded.closed,
                        event_date=excluded.event_date,
                        raw_json=excluded.raw_json
                    """,
                    (
                        market.market_id,
                        market.event_id,
                        market.question,
                        market.slug,
                        1 if market.active else 0,
                        1 if market.closed else 0,
                        market.event_date,
                        market.raw_json,
                    ),
                )
            self._conn.commit()

    def search_markets(self, query: str, limit: int) -> List[MarketRecord]:
        like = f"%{query}%"
        with self._lock:
            cur = self._conn.execute(
                """
                SELECT market_id, event_id, question, slug, active, closed, event_date, raw_json
                FROM markets
                WHERE question LIKE ? OR slug LIKE ?
                LIMIT ?
                """,
                (like, like, limit),
            )
            rows = cur.fetchall()
        return [
            MarketRecord(
                market_id=row[0],
                event_id=row[1],
                question=row[2],
                slug=row[3],
                active=bool(row[4]),
                closed=bool(row[5]),
                event_date=row[6],
                raw_json=row[7],
            )
            for row in rows
        ]

    def get_market(self, market_id: str) -> MarketRecord | None:
        with self._lock:
            cur = self._conn.execute(
                """
                SELECT market_id, event_id, question, slug, active, closed, event_date, raw_json
                FROM markets
                WHERE market_id = ?
                """,
                (market_id,),
            )
            row = cur.fetchone()
        if not row:
            return None
        return MarketRecord(
            market_id=row[0],
            event_id=row[1],
            question=row[2],
            slug=row[3],
            active=bool(row[4]),
            closed=bool(row[5]),
            event_date=row[6],
            raw_json=row[7],
        )

    def get_event_slug(self, event_id: str) -> str | None:
        with self._lock:
            cur = self._conn.execute(
                "SELECT slug FROM events WHERE event_id = ?",
                (event_id,),
            )
            row = cur.fetchone()
        if not row:
            return None
        return row[0]

    def close(self) -> None:
        with self._lock:
            self._conn.close()
