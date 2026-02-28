# ruff: noqa

from uuid import uuid4
from dataclasses import dataclass

Vector = tuple[int, int]

@dataclass
class Entity:
    health: int
    energy: int
    position: tuple[int, int] = (0,0)
    id: str = str(uuid4())

    def move(self, vector: Vector):
        self.position = (self.position[0] + vector[0], self.position[1] + vector[1])

    def harm(self, damage: int):
        self.health -= damage

    def is_dead(self) -> bool:
        return self.health <= 0