"""Stores the handler type alias."""

from typing import Callable
from ..event_types.event import Event

Handler = Callable[[Event], None]
