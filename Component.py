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
    def __init__(self, entity, movement_speed, input_component):
        Component.__init__(self, entity, 'movement')

        self.position = TileManager.pixel_to_tile((entity.x, entity.y))

        self.input_component = input_component
        self.movement_speed = movement_speed
        self.direction = None
        self.target_pos = None

    def move_command(self, direction):
        if not self.target_pos:
            self.set_target(direction)

    def set_target(self, direction):
        self.direction = direction

        direction_vector = Helpers.direction_to_direction_vector(direction)

        next_tile_pos = Helpers.add_vectors(self.position, direction_vector)

        if next_tile_pos == Tile.INVALID_TILE_POSITION:
            Logger.log('can\'t go that way!')
            return

        self.target_pos = next_tile_pos

    def move(self):
        pixel_pos = (self.entity.x, self.entity.y)

        # You have reached your destination

        target_reached = Helpers.vector_equality(pixel_pos, TileManager.tile_to_pixel(self.target_pos))

        if target_reached:
            self.position = self.target_pos
            self.target_pos = None

            direction = self.input_component.continuous_input
            if direction:
                self.set_target(direction)
        else:
            direction_vector = Helpers.direction_to_direction_vector(self.direction)

            self.entity.x += direction_vector[0] * self.movement_speed
            self.entity.y += direction_vector[1] * self.movement_speed

    def update(self):
        Component.update(self)

        input = self.input_component.continuous_input
        if input:
            self.move_command(input)

        if self.target_pos:
            self.move()


class InputComponent(Component):
    def __init__(self, entity, tag):
        Component.__init__(self, entity, tag)
        self.continuous_input = None
        self.event_input = None

    def update(self):
        Component.update(self)


class PlayerInputComponent(InputComponent):
    def __init__(self, entity):
        InputComponent.__init__(self, entity, 'player input')

    def update(self):
        InputComponent.update(self)

        self.event_input = InputHandler.current_event
        self.continuous_input = InputHandler.current_continuous

