"""Event boilerplate."""

from dataclasses import dataclass
from uuid import uuid4
from typing import Any


@dataclass(kw_only=True)
class Event:
    """Event boilerplate.

    Parameters
    ----------
    source : Any
        Stores the object that pushed called the event to be queued.
    priority : int, optional
        Store the priority of the event (higher number means higher priority), by default 0.
    tick_created : int
        Store the tick that the object was created.
    tick_delay : int, optional
        How many dicks need to pass before the event is fired, by default 0.

    """

    source: Any
    priority: int = 0
    tick_created: int
    tick_delay: int = 0
    cancelled: bool = False
    id: str = str(uuid4())
