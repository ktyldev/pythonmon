import pygame
import configuration
import scene

from gui_module import Gui
from input import InputHandler


class Loop:
    def __init__(self):
        self.gui = None
        self.scene = None
        pass

    def setup(self):
        pass

    def tick(self, frame):
        pygame.event.pump()
        InputHandler.event_tick()
        if frame % configuration.event_loop_multiplier:
            self.gui.draw()
            InputHandler.gui_tick()
            InputHandler.clear()

    def run(self, scene_name):
        pygame.init()
        clock = pygame.time.Clock()

        event_loop_tick = configuration.fps * configuration.event_loop_multiplier

        scene.SceneManager.load_scene(scene_name)
        self.scene = scene.SceneManager.scene

        screen_size = configuration.screen_width, configuration.screen_height
        self.gui = Gui(screen_size, configuration.layer_limit)
        self.gui.set_focus('player')
        self.scene.start()

        total_frames = 0
        while True:
            self.tick(total_frames)
            clock.tick(event_loop_tick)
            total_frames += 1
