import pygame

from core import gui, input, scene, overlay
from util import jsonmanager, debug, configuration


def add_input_handlers(config_name):
    path = str(configuration.input_config_path) + config_name + '.json'
    input_config = jsonmanager.get_data(path)

    mapping_objects = input_config['EventMappings']
    for mapping_object in mapping_objects:
        input.add_handler(mapping_object)


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
            debug.log('no assigned tick method')
            return
        self.setup()
        self.total_frames = 0
        debug.log('starting main loop execution')
        while True:
            self.tick_method()
            self.clock.tick(configuration.clock_tick)
            pygame.display.flip()
            self.total_frames += 1

    def set_scene(self, scene_name):
        self.scene = scene.SceneManager.load_scene(scene_name)


class EditorLoop(Loop):
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

            mouse_changed = mouse_input[0] != 'none'
            self.overlay.draw_mouse = mouse_changed

            if mouse_changed:
                debug.log('mouse button down')
                debug.log(mouse_input[0] + ' ' + str(mouse_input[1]))
            else:
                debug.log('mouse button up')

        self.last_tick_mouse = mouse_input[0]

    def run(self):
        if self.scene is None:
            debug.log('scene not set!')
            return
        self.scene.start()
        self.tick_method = self.tick
        super().run()


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
            debug.log('scene not set!')
            return
        self.scene.start()
        self.gui.set_focus('player')
        self.tick_method = self.tick
        super().run()


