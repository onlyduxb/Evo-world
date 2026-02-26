# ruff: noqa

import logging
from collections import defaultdict
from typing import Callable, Type, TypeVar, cast

from decorator_toolkit import log

from ..event_types.event import Event
from ..event_types.handler import Handler

logger = logging.getLogger(__name__)

T = TypeVar("T", bound=Event)


class EventBus:
    def __init__(self):
        self.__subscribers: defaultdict[Type[Event], list[Handler]] = defaultdict(list)
        self.__dispatched: defaultdict[Type[Event] ,list[Handler]] = defaultdict(list)
        self.subscribe(Event, global_listener)

    @log("Subscribed event.")
    def subscribe(self, event_type: Type[T], handler: Callable[[T], None]) -> None:
        self.__subscribers[event_type].append(cast(Handler, handler))

    @log("Unsubscribed event.")
    def unsubscribe_event(self, event_type: Type[Event]) -> None:
        if event_type in self.__subscribers:
            del self.__subscribers[event_type]

    @log("Unsubscribed handler.")
    def unsubscribe_handler(
        self, event_type: Type[T], handler: Callable[[T], None]
    ) -> None:
        if event_type in self.__subscribers:
            self.__subscribers[event_type].remove(cast(Handler, handler))

    @log("Dispatched event.")
    def dispatch(self, event: Event) -> None:
        for cls in type(event).__mro__:
            if cls is object:
                continue
            for handler in self.__subscribers[cls]:
                try:
                    handler(event)
                except Exception:
                    logger.fatal(f"Handler failed while processing {event}")
                self.__dispatched[cls].append(handler)

def global_listener(event: Event):
    logger.debug(f"Global listener heard {event}")
