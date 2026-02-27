# ruff: noqa

from .tile import Tile
from dataclasses import dataclass


@dataclass()
class GroundTile(Tile):
    cell: str = "#"

    def __str__(self) -> str:
        return self.cell