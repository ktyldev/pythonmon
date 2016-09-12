import pygame
import sys


handlers = {}


def tick(name):
    return handlers[name].tick()


def add_handler(handler_mapping_object):
    name = handler_mapping_object['Name']
    mappings = handler_mapping_object['Mappings']
    input_type = handler_mapping_object['Type']

    handler = None
    if input_type == 'keyboard':
        handler = KeyboardInputHandler(mappings)
    elif input_type == 'mouse':
        handler = MouseInputHandler(mappings)

    handlers[name] = handler


class InputHandler:
    def __init__(self, mappings):
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


class KeyboardInputHandler(InputHandler):
    def __init__(self, mappings):
        super().__init__(mappings)

    def tick(self):
        super().tick()

        keys = pygame.key.get_pressed()

        for i in range(0, len(self.inputs)):
            if keys[self.inputs[i]]:
                return self.outputs[i]

        return 'none'


class MouseInputHandler(InputHandler):
    def __init__(self, mappings):
        super().__init__(mappings)

    def tick(self):
        super().tick()

        buttons = pygame.mouse.get_pressed()

        # Currently only handling left and right clicks
        for i in range(0, len(self.inputs)):
            if buttons[self.inputs[i]]:
                return self.outputs[i], pygame.mouse.get_pos()

        return 'none', 'none'
