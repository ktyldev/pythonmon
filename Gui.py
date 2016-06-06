import pygame
import Constants

from Logger import Logger
from Entity import Entity
from Configuration import Configuration
from Component import GraphicsComponent

from Tile import *

class Gui:
    _layer_limit = Configuration.layer_limit
    _log_drawing = Configuration.log_gui
    _screen_width = Configuration.screen_width
    _screen_height = Configuration.screen_height
    _screen = pygame.display.set_mode((_screen_width, _screen_height))
    _draw_tiles = Configuration.draw_tiles
    
    @staticmethod
    def draw():

        # clear the screen
        Gui._screen.fill(Constants.BLACK)

        for layer in range(0, Gui._layer_limit):

            for graphics_component in GraphicsComponent.List:
                if graphics_component.layer == layer:
                    Gui._screen.blit(graphics_component.surface, (graphics_component.draw_x, graphics_component.draw_y))

                    if Gui._log_drawing:
                        Logger.log('Drawing entity ' + entity.name + ' on layer ' + str(layer))
            
            if Gui._draw_tiles:
                for tile in TileManager.List:
                    pygame.draw.rect(Gui._screen, [255, 0, 0], tile)

        # update the display
        pygame.display.flip()