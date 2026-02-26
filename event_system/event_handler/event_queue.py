# ruff: noqa

import logging

from decorator_toolkit import log
from .event_bus import EventBus
from ..event_types.event import Event

logger = logging.getLogger(__name__)


class EventQueue:
    def __init__(self, max_events: int):
        self.max_events: int = max_events
        self.__queue: list[Event] = []

    @log("Appended an event to queue.")
    def append(self, event: Event):
        if self.max_events > len(self.__queue):
            self.__queue.append(event)
        else:
            raise OverflowError

    @log("Popped an event from the queue.")
    def pop(self) -> Event | None:
        try:
            return self.__queue.pop(0)
        except Exception:
            logger.fatal("Failed to pop array")

    @log("Removed an event from the queue.")
    def remove(self, event: Event):
        if event in self.__queue:
            self.__queue.remove(event)

    @log("Peeked the queue.")
    def peek(self) -> Event | None:
        try:
            return self.__queue[0]
        except Exception:
            logger.fatal("Failed to peek array")

    def is_empty(self) -> bool:
        return len(self.__queue) == 0

    @log("Cleared the queue.")
    def clear(self):
        self.__queue = []

    @log("Published events.")
    def publish(self, bus: EventBus):
        events = self.__queue[:]
        events.sort(key=lambda event: event.priority, reverse=True)
        for event in events:
            if event.tick_delay <= 0 and not event.cancelled:
                bus.dispatch(event)
            event.tick_delay -= 1
        self.clean()

    @log("Cleaned the queue.")
    def clean(self):
        self.__queue = [
            event
            for event in self.__queue
            if event.tick_delay >= 0 and not event.cancelled
        ]
