# ruff: noqa

from .event_types.event import Event
from .event_types.handler import Handler
from .event_handler.event_bus import EventBus
from .event_handler.event_queue import EventQueue
from typing import TypeVar, cast, Callable
from decorator_toolkit import log

T = TypeVar("T", bound=Event)

class TickHandler:
    def __init__(self, max_events: int) -> None:
        self.__event_queue: EventQueue = EventQueue(max_events)
        self.__event_bus: EventBus = EventBus()
        self.current_tick = 0

    @log("Scheduled event.")
    def schedule_event(self, event: Event):
        self.__event_queue.append(event)
    
    @log("Processed tick.")
    def process_tick(self):
        self.__event_queue.publish(self.__event_bus)
        self.current_tick += 1

    @log("Registered handler.")
    def register_handler(self, event_type: type[Event], handler: Callable[[T], None]) -> None:
        self.__event_bus.subscribe(event_type, cast(Handler, handler))