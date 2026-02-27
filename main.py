# ruff: noqa
from event_system.event_types.agent_events import AgentAte, AgentDied
from event_system.tick_handler import TickHandler
from entity_system.entity_types.agent import Agent
from logger import setup_logger
from world_system.generation_handler import GenerationHandler

setup_logger()

# -- EXAMPLE CODE (start) --


def death(event: AgentDied) -> None:
    print(f"{event.source.id} died to {event.cause}")


def count(event: AgentDied) -> None:
    print("Added to count")


def fail(event: AgentDied) -> None:
    raise NotImplementedError


def eat(event: AgentAte) -> None:
    print(f"{event.source.id} ate and gained {event.energy_gain} energy")


gen_handler = GenerationHandler(25, 50)
print(gen_handler)
tick_handler: TickHandler = TickHandler(max_events=10)
test_agent = Agent()
tick_handler.subscribe_handler(AgentDied, death)
tick_handler.subscribe_handler(AgentDied, count)
tick_handler.subscribe_handler(AgentAte, eat)
tick_handler.subscribe_handler(AgentDied, fail)





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
