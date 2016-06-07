import Constants

from Component import GraphicsComponent

from Tile import *
from Helpers import Helpers


class Gui:
    _layer_limit = Configuration.layer_limit
    _log_drawing = Configuration.log_gui
    _screen_width = Configuration.screen_width
    _screen_height = Configuration.screen_height
    _screen = pygame.display.set_mode((_screen_width, _screen_height))
    _draw_tiles = Configuration.draw_tiles
    _screen_centre = _screen_width / 2, _screen_height / 2

    focus = None

    @staticmethod
    def set_focus(graphics_component):
        Gui.focus = graphics_component

    @staticmethod
    def draw():
        draw_pos = Gui.focus.draw_x, Gui.focus.draw_y
        V = Helpers.subtract_vector(Gui._screen_centre, draw_pos)

        # clear the screen
        Gui._screen.fill(Constants.BLACK)

        for layer in range(0, Gui._layer_limit):

            for graphics_component in GraphicsComponent.List:
                if graphics_component.layer == layer:

                    draw_rect = graphics_component.draw_x, graphics_component.draw_y
                    draw_with_offset = Helpers.add_vectors(draw_rect, V)

                    Gui._screen.blit(
                        graphics_component.surface, draw_with_offset)

                    if Gui._log_drawing:
                        Logger.log('Drawing entity ' + entity.name + ' on layer ' + str(layer))
            
            if Gui._draw_tiles:
                for tile in TileManager.List:
                    pygame.draw.rect(Gui._screen, [255, 0, 0], tile)

        # update the display
        pygame.display.flip()