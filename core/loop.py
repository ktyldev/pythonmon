import pygame

from core import gui, input, scene, overlay
from util import jsonmanager, logger, configuration


def add_input_handlers(config_name):
    path = str(configuration.input_config_path) + config_name + '.json'
    input_config = jsonmanager.get_data(path)

    mapping_objects = input_config['EventMappings']
    for mapping_object in mapping_objects:
        name = mapping_object['Name']
        mappings = mapping_object['Mappings']

        # TODO: make this less gross
        input_type = input_config['Type']
        if input_type == 'keyboard':
            input.add_keyboard_handler(name, mappings)
        elif input_type == 'mouse':
            input.add_mouse_handler(name, mappings)


class Loop:
    def __init__(self):
        self.clock = None
        self.total_frames = 0
        self.tick_method = None
        self.scene = None

    def setup(self):
        pygame.init()
        self.clock = pygame.time.Clock()

    def run(self):
        if self.tick_method is None:
            logger.log('no assigned tick method')
            return
        self.setup()
        self.total_frames = 0
        logger.log('starting main loop execution')
        while True:
            self.tick_method()
            self.clock.tick(configuration.clock_tick)
            pygame.display.flip()
            self.total_frames += 1

    def set_scene(self, scene_name):
        self.scene = scene.SceneManager.load_scene(scene_name)


class TestLoop(Loop):
    def __init__(self):
        super().__init__()
        self.gui = gui.Gui()
        self.overlay = overlay.Overlay(self.gui.screen)

        add_input_handlers('test-mouse-input')

        self.last_tick_mouse = 'none'

    def tick(self):
        pygame.event.pump()
        self.gui.draw()
        self.overlay.draw()

        mouse_input = input.tick('mouse')
        if mouse_input[0] != self.last_tick_mouse:
            if mouse_input[0] == 'none':
                logger.log('mouse button up')
                self.overlay.draw_mouse = False
            else:
                logger.log('mouse button down')
                logger.log(mouse_input[0] + ' ' + str(mouse_input[1]))
                self.overlay.draw_mouse = True

        self.last_tick_mouse = mouse_input[0]

    def run(self):
        if self.scene is None:
            logger.log('scene not set!')
            return
        self.scene.start()
        self.tick_method = self.tick
        super().run()


class EditorGameLoop(Loop):
    def __init__(self):
        super().__init__()
        self.gui = gui.Gui()

        # input setup


class DefaultGameLoop(Loop):
    def __init__(self):
        super().__init__()
        self.gui = gui.Gui()

        add_input_handlers('overworld-input')

    def tick(self):
        pygame.event.pump()
        event_input = input.tick('event')
        if self.total_frames % configuration.event_loop_multiplier == 0:
            self.gui.draw()
            cont_input = input.tick('continuous')

            self.scene.update(event_input, cont_input)

    def run(self):
        if self.scene is None:
            logger.log('scene not set!')
            return
        self.scene.start()
        self.gui.set_focus('player')
        self.tick_method = self.tick
        super().run()


