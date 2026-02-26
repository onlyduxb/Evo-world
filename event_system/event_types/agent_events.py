# ruff: noqa

from dataclasses import dataclass
from .event import Event
from entity_system.agent_manager import Agent

@dataclass(kw_only=True)
class AgentEvent(Event):
    source: Agent


@dataclass
class AgentDied(AgentEvent):
    cause: str


@dataclass
class AgentAte(AgentEvent):
    energy_gain: int

@dataclass
class AgentReproduced(AgentEvent): ...