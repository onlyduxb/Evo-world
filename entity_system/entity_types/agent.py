# ruff: noqa

from .entity import Entity
from dataclasses import dataclass
from ...item_system.item_types.weapon import Weapon

@dataclass(kw_only=True)
class Agent(Entity):
    health: int = 100
    energy: int = 100
    weapon: Weapon = Weapon(name="fist", damage=15)