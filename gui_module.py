import pygame
import constants

from component_module import GraphicsComponent
from helpers import Helpers


class Gui:
    """
    manages the display of graphics onscreen
    """

    def __init__(self, screen_size, layer_limit):
        screen_width = screen_size[0]
        screen_height = screen_size[1]

        self.layer_limit = layer_limit
        self.screen_centre = screen_width / 2, screen_height / 2
        self.ticks = 0

        self.screen = pygame.display.set_mode(screen_size)

        self.focus = None

    def set_focus(self, entity_name):
        """
        centres view
        :param entity_name: entity to keep at centre of screen
        :return:
        """

        for graphics_component in GraphicsComponent.List:
            if graphics_component.entity.name == entity_name:
                self.focus = graphics_component

    def draw(self):
        """
        draw all enabled GraphicsComponents layer by layer
        :return:
        """

        # clear the screen
        self.screen.fill(constants.BLACK)

        for layer in range(0, self.layer_limit):
            for graphics_component in GraphicsComponent.List:
                if graphics_component.layer == layer and graphics_component.enabled:

                    camera_offset = self.get_camera_offset()
                    draw_rect = graphics_component.draw_x, graphics_component.draw_y
                    draw_with_offset = Helpers.add_vectors(camera_offset, draw_rect)

                    self.screen.blit(graphics_component.surface, draw_with_offset)

        self.ticks += 1
        pygame.display.flip()

    def get_camera_offset(self):
        draw_pos = self.screen_centre
        if self.focus:
            draw_pos = self.focus.draw_x, self.focus.draw_y
        camera_offset = Helpers.subtract_vector(self.screen_centre, draw_pos)
        return camera_offset
