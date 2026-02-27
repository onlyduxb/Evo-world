# ruff: noqa

from .entity import Entity
from dataclasses import dataclass

@dataclass
class Agent(Entity):
    health: int = 100
    energy: int = 100
    
