import pygame
import sys

import configuration

handlers = {}
path = configuration.input_config_path

def tick(name):
    return handlers[name].tick()


def add_handler(name, mappings):
    handler = KeyboardInputHandler(mappings)
    handlers[name] = handler


class KeyboardInputHandler:
    def __init__(self, mappings):
        self.__path = configuration.input_config_path
        self.inputs = []
        self.outputs = []
        for mapping in mappings:
            self.inputs.append(mapping['KeyCode'])
            self.outputs.append(mapping['Input'])

    def tick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        for i in range(0, len(self.inputs)):
            if keys[self.inputs[i]]:
                return self.outputs[i]

        return 'none'

    @property
    def path(self):
        return self.__path
