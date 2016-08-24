import pygame
import configuration
import scene
import logger

from gui_module import Gui
from input import InputManager


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


class DefaultGameLoop(Loop):
    def __init__(self):
        super().__init__()
        screen_size = configuration.screen_width, configuration.screen_height
        self.gui = Gui(screen_size, configuration.layer_limit)
        self.input_manager = InputManager()
        self.scene = None

    def tick(self):
        pygame.event.pump()
        event_input = self.input_manager.dict_tick('event')
        if self.total_frames % configuration.event_loop_multiplier == 0:
            self.gui.draw()
            cont_input = self.input_manager.dict_tick('continuous')

            self.scene.update(event_input, cont_input)

    def run(self):
        self.scene.start()
        self.gui.set_focus('player')
        self.tick_method = self.tick
        super().run()

    def set_scene(self, scene_name):
        scene.SceneManager.load_scene(scene_name)
        self.scene = scene.SceneManager.scene
