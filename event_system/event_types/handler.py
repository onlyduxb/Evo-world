# ruff: noqa

from typing import Callable
from ..event_types.event import Event

Handler = Callable[[Event], None]
