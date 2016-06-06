import pygame

from Tile import *
from Helpers import Helpers
from Logger import Logger
from Input import *


class Component:

    List = []

    @staticmethod
    def find(tag):
        for component in Component.List:
            if component.tag == tag:
                return component
        return None

    def __init__(self, entity, tag):
        self.entity = entity
        self.enabled = True
        self.tag = tag
        Component.List.append(self)

    def update(self):
        return


class GraphicsComponent(Component):

    List = []

    def __init__(self, entity, image, layer):
        Component.__init__(self, entity, 'graphics')

        self.draw_x = 0
        self.draw_y = 0

        self.layer = layer
        self.surface = pygame.image.load(image)
        GraphicsComponent.List.append(self)

    def update(self):
        Component.update(self)
        self.draw_x = self.entity.x
        self.draw_y = self.entity.y


class MovementComponent(Component):
    def __init__(self, entity, movement_speed):
        Component.__init__(self, entity, 'movement')

        self.position = TileManager.pixel_to_tile((entity.x, entity.y))

        self.movement_speed = movement_speed
        self.direction_vector = None
        self.target_pos = None

    def set_target(self, direction_vector):
        next_tile_pos = Helpers.add_vectors(self.position, direction_vector)

        if next_tile_pos == Tile.INVALID_TILE_POSITION:
            Logger.log('can\'t go that way!')
            return

        self.target_pos = next_tile_pos
        self.direction_vector = direction_vector

    def remove_target(self):
        self.target_pos = None

    def move(self):
        pixel_pos = (self.entity.x, self.entity.y)

        if TileManager.pixel_to_tile(pixel_pos) == self.target_pos:
            self.remove_target()
            return

        self.entity.x += self.direction_vector[0] * self.movement_speed
        self.entity.y += self.direction_vector[1] * self.movement_speed

    def update(self):
        Component.update(self)
        if self.target_pos:
            self.move()


class InputComponent(Component):
    def __init__(self, entity):
        Component.__init__(self, entity, 'input')
        self.continuous_input = None
        self.event_input = None

    def update(self):
        Component.update(self)

        self.event_input = InputHandler.current_event
        self.continuous_input = InputHandler.current_continuous
