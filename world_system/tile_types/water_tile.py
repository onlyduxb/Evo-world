# ruff: noqa

from .tile import Tile
from dataclasses import dataclass


@dataclass()
class WaterTile(Tile):
    cell: str = "~"
    energy_consumption: int = 25
