# ruff: noqa
from event_system.event_handler.event_bus import EventBus
from event_system.event_handler.event_queue import EventQueue
from event_system.events.agent_events import AgentAte, AgentDied
from entity_system.agent_manager import Agent
from logger import setup_logger

setup_logger()

# -- EXAMPLE CODE (start) --


def death(event: AgentDied) -> None:
    print(f"{event.source.agent_id} died to {event.cause}")


def count(event: AgentDied) -> None:
    print("Added to count")


def fail(event: AgentDied) -> None:
    raise NotImplementedError


def eat(event: AgentAte) -> None:
    print(f"{event.source.agent_id} ate and gained {event.energy_gain} energy")



current_tick = 0
test_agent = Agent()
b: EventBus = EventBus()
q: EventQueue = EventQueue(10)
b.subscribe(AgentDied, death)
b.subscribe(AgentDied, count)
b.subscribe(AgentAte, eat)
b.subscribe(AgentDied, fail)
q.append(
    AgentAte(energy_gain=15, source=test_agent, tick_created=current_tick, priority=2)
)
q.append(
    AgentDied(
        cause="starvation",
        source=test_agent,
        tick_created=current_tick,
        tick_delay=2,
        priority=0,
    )
)
# b.unsubscribe_event(AgentDied)
while True:
    input("Press enter to complete tick")
    q.publish(b)


# -- EXAMPLE CODE (end) --
