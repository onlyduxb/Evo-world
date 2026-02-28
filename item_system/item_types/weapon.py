# ruff: noqa

from .item import Item
from dataclasses import dataclass


@dataclass(kw_only=True)
class Weapon(Item):
    damage: int
