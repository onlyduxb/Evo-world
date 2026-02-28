# ruff: noqa

from .tile import Tile
from dataclasses import dataclass


@dataclass()
class GroundTile(Tile):
    cell: str = "#"
    energy_consumption: int = 10