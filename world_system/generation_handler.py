# ruff: noqa

from .generation.world_generator import WorldGenerator
from .tile_types.tile import Tile

class GenerationHandler:
    def __init__(self, world_height: int = 25, world_width: int = 50) -> None:
        self.__world_generator: WorldGenerator = WorldGenerator(world_width=world_width, world_height=world_height)
        self.map: list[list[Tile]] = self.__world_generator.map

    def __str__(self) -> str:
        return '\n'.join(' '.join(str(tile) for tile in row) for row in self.map)
    