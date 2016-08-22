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


class KeyboardInputHandler:
    def __init__(self):
        self.current = None
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
                self.current = self.outputs[i]

    def clear(self):
        self.current = None


class InputHandler:
    current_event = None
    current_continuous = None

    event_handler = KeyboardInputHandler()
    event_handler.add_mapping(pygame.K_z, KeyboardInputType.A)
    event_handler.add_mapping(pygame.K_x, KeyboardInputType.B)
    event_handler.add_mapping(pygame.K_c, KeyboardInputType.START)
    event_handler.add_mapping(pygame.K_v, KeyboardInputType.SELECT)

    continuous_handler = KeyboardInputHandler()
    continuous_handler.add_mapping(pygame.K_LEFT, KeyboardInputType.LEFT)
    continuous_handler.add_mapping(pygame.K_UP, KeyboardInputType.UP)
    continuous_handler.add_mapping(pygame.K_RIGHT, KeyboardInputType.RIGHT)
    continuous_handler.add_mapping(pygame.K_DOWN, KeyboardInputType.DOWN)

    @staticmethod
    def event_tick():
        InputHandler.current_event = InputHandler.tick(InputHandler.event_handler)

    @staticmethod
    def gui_tick():
        InputHandler.current_continuous = InputHandler.tick(InputHandler.continuous_handler)

    @staticmethod
    def tick(handler):
        handler.tick()
        return handler.current

    @staticmethod
    def clear():
        InputHandler.event_handler.clear()
        InputHandler.continuous_handler.clear()

    '''
    @staticmethod
    def event_tick():

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_z]:
            InputHandler.current_event = KeyboardInputType.A
        elif keys[pygame.K_x]:
            InputHandler.current_event = KeyboardInputType.B
        elif keys[pygame.K_c]:
            InputHandler.current_event = KeyboardInputType.START
        elif keys[pygame.K_v]:
            InputHandler.current_event = KeyboardInputType.SELECT

    @staticmethod
    def gui_tick():

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            InputHandler.current_continuous = KeyboardInputType.UP
        elif keys[pygame.K_RIGHT]:
            InputHandler.current_continuous = KeyboardInputType.RIGHT
        elif keys[pygame.K_DOWN]:
            InputHandler.current_continuous = KeyboardInputType.DOWN
        elif keys[pygame.K_LEFT]:
            InputHandler.current_continuous = KeyboardInputType.LEFT

    @staticmethod
    def clear():
        InputHandler.current_event = None
        InputHandler.current_continuous = None'''
