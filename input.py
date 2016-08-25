import pygame
import sys


handlers = {}


def tick(name):
    return handlers[name].tick()


def add_handler(name, mappings):
    handler = KeyboardInputHandler(mappings)
    handlers[name] = handler


class KeyboardInputHandler:
    def __init__(self, mappings):
        self.inputs = []
        self.outputs = []
        for mapping in mappings:
            self.inputs.append(mapping[0])
            self.outputs.append(mapping[1])

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
