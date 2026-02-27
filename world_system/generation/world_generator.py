# ruff: noqa

import numpy as np
import numpy.typing as npt
from scipy.ndimage import gaussian_filter  # type: ignore
from ..tile_types.tile import Tile
from ..tile_types.ground_tile import GroundTile
from ..tile_types.water_tile import WaterTile


class WorldGenerator:
    def __init__(self, world_height: int = 50, world_width: int = 25):
        self.world_width: int = world_width
        self.world_height: int = world_height
        self.map: list[list[Tile]] = self.generate_map()

    def generate_map(self) -> list[list[Tile]]:
        x: npt.NDArray[np.float64] = np.random.uniform(
            0, 1, (self.world_height, self.world_width)
        )
        x = gaussian_filter(x, sigma=1).astype(np.float64)
        mask = x > 0.5

        return [
            [
                GroundTile() if mask[i, j] else WaterTile()
                for j in range(self.world_width)
            ]
            for i in range(self.world_height)
        ]

