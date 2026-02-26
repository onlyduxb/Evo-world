# ruff: noqa

from dataclasses import dataclass
from uuid import uuid4
from typing import Any


@dataclass(kw_only=True)
class Event:
    source: Any
    tick_created: int
    priority: int = 0
    tick_delay: int = 0
    cancelled: bool = False
    id: str = str(uuid4())
