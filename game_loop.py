import pygame
import configuration
import scene
import logger
import input

from gui_module import Gui


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

        ev_mappings = [[122, 'a'], [120, 'b'], [99, 'start'], [118, 'select']]
        co_mappings = [[276, 'left'], [273, 'up'], [275, 'right'], [274, 'down']]

        input.add_handler('event', ev_mappings)
        input.add_handler('continuous', co_mappings)

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

    def set_scene(self, scene_name):
        self.scene = scene.SceneManager.load_scene(scene_name)
