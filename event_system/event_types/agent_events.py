"""Agent events."""

from dataclasses import dataclass
from .event import Event
from entity_system.entity_types.agent import Agent


@dataclass(kw_only=True)
class AgentEvent(Event):
    """AgentEvent boilerplate, parent class is event (source : Agent)."""

    source: Agent


@dataclass
class AgentDied(AgentEvent):
    """Death event.

    Parameters
    ----------
    cause : str
        Cause of death.

    """

    cause: str


@dataclass
class AgentAte(AgentEvent):
    """Agent ate event.

    Parameters
    ----------
    energy_gain : int
        The amount of energy gained.

    """

    energy_gain: int


@dataclass
class AgentReproduced(AgentEvent):
    """Agent reproduced event."""

    ...
