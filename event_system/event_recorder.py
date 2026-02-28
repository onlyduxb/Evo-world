# ruff: noqa

from typing import TypeVar
from collections import defaultdict
from .event_types.event import Event

T = TypeVar("T", bound=Event)

class EventRecorder:
    def __int__(self):
        self.__recorded_events: defaultdict[int, list[Event]] = defaultdict(list)

    def record_event(self, tick: int, event: Event):
        self.__recorded_events[tick].append(event)

    def get_record(self) -> defaultdict[int, list[Event]]:
        return self.__recorded_events
