# ruff: noqa
from event_system.event_types.agent_events import AgentAte, AgentDied
from event_system.tick_handler import TickHandler
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


tick_handler: TickHandler = TickHandler(10)
test_agent = Agent()
tick_handler.register_handler(AgentDied, death)
tick_handler.register_handler(AgentDied, count)
tick_handler.register_handler(AgentAte, eat)
tick_handler.register_handler(AgentDied, fail)
tick_handler.schedule_event(
    AgentAte(
        energy_gain=15,
        source=test_agent,
        tick_created=tick_handler.current_tick,
        priority=2,
    )
)
tick_handler.schedule_event(
    AgentDied(
        cause="starvation",
        source=test_agent,
        tick_created=tick_handler.current_tick,
        tick_delay=2,
        priority=0,
    )
)
# b.unsubscribe_event(AgentDied)
while True:
    input("Press enter to complete tick")
    tick_handler.process_tick()


# -- EXAMPLE CODE (end) --
