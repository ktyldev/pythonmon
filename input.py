import pygame
import sys


class KeyboardInputType:
    A = 'a'
    B = 'b'
    START = 'start'
    SELECT = 'select'
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'
    NONE = 'none'


class KeyboardInputHandler:
    def __init__(self):
        self.inputs = []
        self.outputs = []

    def add_mapping(self, input_key, output):
        self.inputs.append(input_key)
        self.outputs.append(output)

    def tick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        for i in range(0, len(self.inputs)):
            if keys[self.inputs[i]]:
                return self.outputs[i]
        return KeyboardInputType.NONE


class InputManager:
    def __init__(self):
        self.handlers = {}

        # TODO: don't hardcode this stuff
        event_handler = KeyboardInputHandler()
        event_handler.add_mapping(pygame.K_z, KeyboardInputType.A)
        event_handler.add_mapping(pygame.K_x, KeyboardInputType.B)
        event_handler.add_mapping(pygame.K_c, KeyboardInputType.START)
        event_handler.add_mapping(pygame.K_v, KeyboardInputType.SELECT)
        self.register_handler(event_handler, 'event')

        continuous_handler = KeyboardInputHandler()
        continuous_handler.add_mapping(pygame.K_LEFT, KeyboardInputType.LEFT)
        continuous_handler.add_mapping(pygame.K_UP, KeyboardInputType.UP)
        continuous_handler.add_mapping(pygame.K_RIGHT, KeyboardInputType.RIGHT)
        continuous_handler.add_mapping(pygame.K_DOWN, KeyboardInputType.DOWN)
        self.register_handler(continuous_handler, 'continuous')

    def register_handler(self, handler, name):
        self.handlers[name] = handler

    def dict_tick(self, handler_name):
        handler = self.handlers[handler_name]
        return handler.tick()
