import pygame
import sys


class InputType:
    A = 'a'
    B = 'b'
    START = 'start'
    SELECT = 'select'
    LEFT = 'left'
    UP = 'up'
    RIGHT = 'right'
    DOWN = 'down'


class InputHandler:

    current_event = None
    current_continuous = None

    @staticmethod
    def event_tick():

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_z]:
            InputHandler.current_event = InputType.A
        elif keys[pygame.K_x]:
            InputHandler.current_event = InputType.B
        elif keys[pygame.K_c]:
            InputHandler.current_event = InputType.START
        elif keys[pygame.K_v]:
            InputHandler.current_event = InputType.SELECT

    @staticmethod
    def gui_tick():

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            InputHandler.current_continuous = InputType.UP
        elif keys[pygame.K_RIGHT]:
            InputHandler.current_continuous = InputType.RIGHT
        elif keys[pygame.K_DOWN]:
            InputHandler.current_continuous = InputType.DOWN
        elif keys[pygame.K_LEFT]:
            InputHandler.current_continuous = InputType.LEFT

    @staticmethod
    def clear():
        InputHandler.current_event = None
        InputHandler.current_continuous = None
