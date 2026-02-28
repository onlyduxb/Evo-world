# ruff: noqa

from dataclasses import dataclass


@dataclass(kw_only=True, repr=False)
class Tile:
    cell: str
    energy_consumption: int = 0

    def __str__(self) -> str:
        return self.cell