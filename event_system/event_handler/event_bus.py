"""Event bus."""

import logging
from collections import defaultdict
from typing import Callable, Type, TypeVar, cast

from ..event_types.event import Event
from ..event_types.handler import Handler
from ..event_recorder import EventRecorder
logger = logging.getLogger(__name__)

T = TypeVar("T", bound=Event)


class EventBus:
    """Event bus runs subscribed events."""

    def __init__(self):
        """__init__ Initialise a bus."""
        self.__subscribers: defaultdict[Type[Event], list[Handler]] = defaultdict(list)
        self.__event_recorder: EventRecorder = EventRecorder()
        self.subscribe_handler(Event, global_listener)

    def subscribe_event(self, event_type: Type[T]):
        """Subscribe subscribe an event type to the subscribers list.

        Parameters
        ----------
        event_type : Type[Event]
            Event class.
    
        """
        if event_type not in self.__subscribers:
            self.__subscribers[event_type] = []

    def unsubscribe_event(self, event_type: Type[Event]) -> None:
        """Unsubscribe_event unsubscribe an event type from the subscribers list.

        Parameters
        ----------
        event_type : Type[Event]
            Event class.

        """
        if event_type in self.__subscribers:
            del self.__subscribers[event_type]

    def subscribe_handler(self, event_type: Type[T], handler: Callable[[T], None]) -> None:
        """Subscribe an event to the subscribers.

        Parameters
        ----------
        event_type : Type[T]
            Event class.
        handler : Callable[[T], None]
            Function that runs on event.

        """
        self.__subscribers[event_type].append(cast(Handler, handler))


    def unsubscribe_handler(
        self, event_type: Type[T], handler: Callable[[T], None]
    ) -> None:
        """Unsubscribe_handler unsubscribes an event handler from the subscribers.

        Parameters
        ----------
        event_type : Type[T]
            Event class.
        handler : Callable[[T], None]
            Function that runs on event.

        """
        if event_type in self.__subscribers:
            self.__subscribers[event_type].remove(cast(Handler, handler))

    def dispatch(self, current_tick: int, event: Event) -> None:
        """Run all of the handlers on the given event.

        Parameters
        ----------
        current_tick : int
            The current tick of the simulation.
        event : Event
            Event to run handlers on.

        """
        self.__event_recorder.record_event(current_tick, event)
        for cls in type(event).__mro__:
            if cls is object:
                continue
            for handler in self.__subscribers[cls]:
                try:
                    handler(event)
                except Exception:
                    logger.fatal(f"Handler failed while processing {event}")



def global_listener(event: Event):
    """global_listener Listens to all events.

    Parameters
    ----------
    event : Event
        An event.

    """
    logger.debug(f"Global listener heard {event}")
