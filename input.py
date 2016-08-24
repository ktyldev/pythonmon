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

    def add_mappings(self, mappings):
        """
        adds many input mappings
        :param mappings: key-value pairs [pygame keycode, input type]
        :return:
        """
        for mapping in mappings:
            key = mapping[0]
            input_type = mapping[1]
            self.add_mapping(key, input_type)

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
        event_mappings = [
            [122, 'a'],
            [120, 'b'],
            [99, 'start'],
            [118, 'select']
        ]
        event_handler.add_mappings(event_mappings)
        '''
        event_handler.add_mapping(pygame.K_z, KeyboardInputType.A) # 122
        event_handler.add_mapping(pygame.K_x, KeyboardInputType.B)  # 120
        event_handler.add_mapping(pygame.K_c, KeyboardInputType.START) # 99
        event_handler.add_mapping(pygame.K_v, KeyboardInputType.SELECT) # 118
        '''
        self.register_handler(event_handler, 'event')

        continuous_handler = KeyboardInputHandler()
        cont_mappings = [
            [276, 'left'],
            [273, 'up'],
            [275, 'right'],
            [274, 'down']
        ]
        continuous_handler.add_mappings(cont_mappings)

        '''
        continuous_handler.add_mapping(pygame.K_LEFT, KeyboardInputType.LEFT) # 276
        continuous_handler.add_mapping(pygame.K_UP, KeyboardInputType.UP) # 273
        continuous_handler.add_mapping(pygame.K_RIGHT, KeyboardInputType.RIGHT) # 275
        continuous_handler.add_mapping(pygame.K_DOWN, KeyboardInputType.DOWN) # 274
        '''
        self.register_handler(continuous_handler, 'continuous')

    def register_handler(self, handler, name):
        self.handlers[name] = handler

    def dict_tick(self, handler_name):
        handler = self.handlers[handler_name]
        return handler.tick()
