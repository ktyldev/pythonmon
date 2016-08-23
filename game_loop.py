import pygame
import configuration
import scene

from gui_module import Gui
from input import InputManager
from logger import Logger


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
            Logger.log('no assigned tick method')
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
        self.screen_width = configuration.screen_width
        self.screen_height = configuration.screen_height
        screen_size = self.screen_width, self.screen_height
        self.gui = Gui(screen_size, configuration.layer_limit)
        self.scene = None

    def tick(self):
        pygame.event.pump()
        event_input = InputManager.event_tick()
        if self.total_frames % configuration.event_loop_multiplier == 0:
            self.gui.draw()
            cont_input = InputManager.gui_tick()

            self.scene.update(event_input, cont_input)

    def run(self):
        self.scene.start()
        self.gui.set_focus('player')
        self.tick_method = self.tick
        super().run()

    def set_scene(self, scene_name):
        scene.SceneManager.load_scene(scene_name)
        self.scene = scene.SceneManager.scene
