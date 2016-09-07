import pygame
from util import configuration, logger, helpers
from model import tile


class Overlay:
    def __init__(self, screen):
        self.screen = screen

        self.draw_tiles = True
        self.draw_mouse = False

    def draw_tile(self, screen_pos, colour):
        side_length = configuration.tile_size
        rect = pygame.Rect(screen_pos, (side_length, side_length))
        pygame.draw.rect(self.screen, colour, rect, 2)

    def draw(self):
        if self.draw_tiles:
            tile_map = tile.Map.current
            if tile_map:
                for i in range(0, tile_map.tile_count()):
                    tile_pos = tile_map.id_to_coord(i)
                    tile_type = tile_map.get_tile_type(tile_pos)

                    if tile_type != 'empty':
                        colour = helpers.colour_from_tile_type(tile_type)

                        screen_pos = helpers.multiply_vector(tile_pos, configuration.tile_size)

                        self.draw_tile(screen_pos, colour)

            else:
                logger.log('no tile map to draw')
        if self.draw_mouse:
            pygame.draw.circle(self.screen, (0, 0, 0), pygame.mouse.get_pos(), 5)

