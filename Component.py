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

    def set_direction_vector(self, direction):
        if direction == 'up':
            self.direction_vector = 0, -1
        elif direction == 'right':
            self.direction_vector = 1, 0
        elif direction == 'down':
            self.direction_vector = 0, 1
        elif direction == 'left':
            self.direction_vector = -1, 0

    def move_command(self, direction):
        if not self.target_pos:
            self.set_direction_vector(direction)
            self.set_target()

    def set_target(self):
        next_tile_pos = Helpers.add_vectors(self.position, self.direction_vector)

        if next_tile_pos == Tile.INVALID_TILE_POSITION:
            Logger.log('can\'t go that way!')
            return

        self.target_pos = next_tile_pos
        Logger.log('Target Set: ' + str(next_tile_pos))

    def move(self):
        pixel_pos = (self.entity.x, self.entity.y)

        # You have reached your destination
        if Helpers.vector_equality(pixel_pos, TileManager.tile_to_pixel(self.target_pos)):
            self.position = self.target_pos
            self.target_pos = None
        else:
            self.entity.x += self.direction_vector[0] * self.movement_speed
            self.entity.y += self.direction_vector[1] * self.movement_speed

    def update(self):
        Component.update(self)
        if self.target_pos:
            self.move()


class PlayerInputComponent(Component):
    def __init__(self, entity, movement_component):
        Component.__init__(self, entity, 'input')
        self.continuous_input = None
        self.event_input = None
        self.movement_component = movement_component

    def update(self):
        Component.update(self)

        self.event_input = InputHandler.current_event
        self.continuous_input = InputHandler.current_continuous

        if self.continuous_input:
            self.movement_component.move_command(self.continuous_input)
