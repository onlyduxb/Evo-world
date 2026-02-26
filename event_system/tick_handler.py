# ruff: noqa

from event_types.event import Event
from event_handler.event_bus import EventBus
from event_handler.event_queue import EventQueue
from event_types.handler import Handler

class TickHandler:
    def __init__(self, max_events: int) -> None:
        self.__event_queue: EventQueue = EventQueue(max_events)
        self.__event_bus: EventBus = EventBus()

    def schedule_event(self, event: Event):
        self.__event_queue.append(event)
    
    def process_tick(self):
        self.__event_queue.publish(self.__event_bus)

    def register_handler(self, event_type: type[Event], handler: Handler) -> None:
        self.__event_bus.subscribe(event_type, handler)