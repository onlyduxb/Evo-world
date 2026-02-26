"""Event queue."""

import logging

from decorator_toolkit import log
from .event_bus import EventBus
from ..event_types.event import Event

logger = logging.getLogger(__name__)


class EventQueue:
    """Event queue that captures all events and dispatches them after each tick."""

    def __init__(self, max_events: int):
        """__init__ Initialise queue.

        Parameters
        ----------
        max_events : int
            Maximum number of events that can happen per tick.

        """
        self.max_events: int = max_events
        self.__queue: list[Event] = []

    @log("Appended an event to queue.")
    def append(self, event: Event):
        """Append an event to the queue.

        Parameters
        ----------
        event : Event
            Event.

        """
        self.sort_queue()
        if self.max_events > len(self.__queue):
            self.__queue.append(event)
        else:
            logger.fatal("Event queue full")

    @log("Popped an event from the queue.")
    def pop(self) -> Event | None:
        """Remove the first event in the queue.

        Returns
        -------
        Event | None
            If the pop operation can not be completed None is returned.

        """
        try:
            return self.__queue.pop(0)
        except Exception:
            logger.fatal("Failed to pop array")

    @log("Removed an event from the queue.")
    def remove(self, event: Event):
        """Remove a specific event from the queue.

        Parameters
        ----------
        event : Event
            Event to be removed from the queue.

        """
        if event in self.__queue:
            self.__queue.remove(event)

    @log("Peeked the queue.")
    def peek(self) -> Event | None:
        """Peek the top item in the queue.

        Returns
        -------
        Event | None
            If the peek operation can not be completed then returns None.

        """
        try:
            return self.__queue[0]
        except Exception:
            logger.fatal("Failed to peek array")

    def is_empty(self) -> bool:
        """Check if the queue is empty.

        Returns
        -------
        bool
            True when the queue is empty.

        """
        return len(self.__queue) == 0

    @log("Cleared the queue.")
    def clear(self):
        """Clear the queue."""
        self.__queue = []

    @log("Published events.")
    def publish(self, bus: EventBus):
        """Publish the queue to an event bus.

        Parameters
        ----------
        bus : EventBus
            Event bus.

        """
        self.sort_queue()
        events = self.__queue[:]
        for event in events:
            if event.tick_delay <= 0 and not event.cancelled:
                bus.dispatch(event)
            event.tick_delay -= 1
        self.clean()

    @log("Cleaned the queue.")
    def clean(self):
        """Remove any events that have fired or been cancelled."""
        self.__queue = [
            event
            for event in self.__queue
            if event.tick_delay >= 0 and not event.cancelled
        ]

    @log("Sorted queue")
    def sort_queue(self):
        """Sort the queue ordering by priority."""
        self.__queue.sort(key=lambda event: event.priority, reverse=True)
