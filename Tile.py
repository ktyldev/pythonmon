import pygame

from Configuration import Configuration
from Logger import Logger


class Tile(pygame.Rect):
    def __init__(self, number, position, size):
        super().__init__((position[0], position[1]), (size[0], size[1]))
        self.id = number


class TileManager:
    TILE_SIZE = Configuration.tile_size
    INVALID_TILE_POSITION = -1, -1

    map_width = 0
    map_height = 0

    List = []

    @staticmethod
    def pixel_to_tile(vector):
        return vector[0] / TileManager.TILE_SIZE, vector[1] / TileManager.TILE_SIZE
    
    @staticmethod
    def tile_to_pixel(vector):
        return vector[0] * TileManager.TILE_SIZE, vector[1] * TileManager.TILE_SIZE

    @staticmethod
    def in_bounds(tile_position):
        x = tile_position[0]
        y = tile_position[1]

        valid_x_range = range(0, TileManager.map_width)
        valid_y_range = range(0, TileManager.map_height)

        return x in valid_x_range and y in valid_y_range

    @staticmethod
    def load_tiles(rect):
        tile_size = TileManager.TILE_SIZE

        TileManager.map_width = rect.width // tile_size
        TileManager.map_height = rect.height // tile_size

        if not rect.width % tile_size == 0 or not rect.width % tile_size == 0:
            raise Exception('rect is of incorrect size')

        Logger.log('Map Height: ' + str(TileManager.map_height) + ' Map Width: ' + str(TileManager.map_width))

        tile_count = 0
        for h in range(0, TileManager.map_height):
            for w in range(0, TileManager.map_width):

                position = (w * tile_size, h * tile_size)
                size = (tile_size, tile_size)

                TileManager.List.append(
                    Tile(
                        tile_count, 
                        position, 
                        size))

                tile_count += 1

        Logger.log('Tiles created: ' + str(tile_count))
