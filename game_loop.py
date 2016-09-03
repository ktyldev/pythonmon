import pygame
import configuration
import jsonmanager
import scene
import logger
import input
import gui


def add_input_handlers(config_name):
    path = str(configuration.input_config_path) + config_name + '.json'
    input_config = jsonmanager.get_data(path)

    mapping_objects = input_config['EventMappings']
    for mapping_object in mapping_objects:
        name = mapping_object['Name']
        mappings = mapping_object['Mappings']

        type = input_config['Type']
        if type == 'keyboard':
            input.add_keyboard_handler(name, mappings)
        elif type == 'mouse':
            input.add_mouse_handler(name, mappings)


class Loop:
    def __init__(self):
        self.clock = None
        self.total_frames = 0
        self.tick_method = None

    def setup(self):
        pygame.init()
        self.clock = pygame.time.Clock()

    def run(self):
        if self.tick_method is None:
            logger.log('no assigned tick method')
            return
        self.setup()
        self.total_frames = 0
        while True:
            self.tick_method()
            self.clock.tick(configuration.clock_tick)
            self.total_frames += 1

    def set_scene(self, scene_name):
        self.scene = scene.SceneManager.load_scene(scene_name)


class TestLoop(Loop):
    def __init__(self):
        super().__init__()
        self.gui = gui.Gui()

        add_input_handlers('test-mouse-input')

        self.scene = None

    def tick(self):
        pygame.event.pump()
        self.gui.draw()
        mouse_input = input.tick('mouse')
        

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

        self.scene = None

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


