import pygame

from Configuration import Configuration
from Logger import Logger

class Tile(pygame.Rect):

    INVALID_TILE_POSITION = (-1, -1)

    def __init__(self, id, position, size):
        self.id = id
        self.position = position
        self.size = size

class TileManager():
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)

    _tile_size = Configuration.tile_size

    map_width = 0
    map_height = 0

    List = []

    @staticmethod
    def pixel_to_tile(vector):
        return (vector[0] / TileManager._tile_size, vector[1] / TileManager._tile_size)
    
    @staticmethod
    def tile_to_pixel(x, y):
        return (x * TileManager._tile_size, y * TileManager._tile_size)

    @staticmethod
    def load_tiles(rect):
        tile_size = TileManager._tile_size

        TileManager.map_width = rect.width / tile_size
        TileManager.map_height = rect.height / tile_size

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