# ruff: noqa

from uuid import uuid4
from dataclasses import dataclass

@dataclass
class Entity:
    health: int
    energy: int
    position: tuple[int, int] = (0,0)
    id: str = str(uuid4())
