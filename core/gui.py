import pygame

from controller.component import GraphicsComponent
from util import configuration, helpers


class Gui:
    """
    manages the display of graphics onscreen
    """
    BLACK = (0, 0, 0)

    def __init__(self):
        self.width = configuration.screen_width
        self.height = configuration.screen_height
        screen_size = self.width, self.height

        self.layer_limit = configuration.layer_limit
        self.screen_centre = self.width / 2, self.height / 2
        self.ticks = 0

        self.screen = pygame.display.set_mode(screen_size)

        self.focus = None
        self.editor_mode = False

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
        self.screen.fill(Gui.BLACK)

        for layer in range(0, self.layer_limit):
            for graphics_component in GraphicsComponent.List:
                if graphics_component.layer == layer and graphics_component.enabled:
                    self.draw_graphics_component(graphics_component)

        self.ticks += 1

    def draw_graphics_component(self, graphics_component):
        camera_offset = self.get_camera_offset()
        draw_rect = graphics_component.draw_x, graphics_component.draw_y
        draw_with_offset = helpers.add_vectors(camera_offset, draw_rect)

        self.screen.blit(graphics_component.surface, draw_with_offset)

    def get_camera_offset(self):
        draw_pos = self.screen_centre
        if self.focus:
            draw_pos = self.focus.draw_x, self.focus.draw_y
        camera_offset = helpers.subtract_vector(self.screen_centre, draw_pos)
        return camera_offset

