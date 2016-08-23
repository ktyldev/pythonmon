import pygame
import configuration
import scene

from gui_module import Gui
from input import InputHandler
from logger import Logger


class Loop:
    def __init__(self):
        self.clock = None
        self.clock_tick = configuration.fps * configuration.event_loop_multiplier
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
            self.clock.tick(self.clock_tick)
            self.total_frames += 1


class DefaultGameLoop(Loop):
    def __init__(self):
        super().__init__()
        self.screen_width = configuration.screen_width
        self.screen_height = configuration.screen_height
        self.gui = Gui((self.screen_width, self.screen_height), configuration.layer_limit)
        self.scene = None

    def tick(self):
        pygame.event.pump()
        InputHandler.event_tick()
        if self.total_frames % configuration.event_loop_multiplier == 0:
            self.gui.draw()
            self.scene.update()
            InputHandler.gui_tick()
            InputHandler.clear()

    def run(self):
        self.scene.start()
        self.gui.set_focus('player')
        self.tick_method = self.tick
        super().run()

    def set_scene(self, scene_name):
        scene.SceneManager.load_scene(scene_name)
        self.scene = scene.SceneManager.scene
