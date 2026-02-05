from __future__ import annotations

import threading


def make_lock() -> threading.Lock:
    return threading.Lock()
