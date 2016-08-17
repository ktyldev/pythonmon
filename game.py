import pygame
import gui
import configuration
import scenemodule
from input import InputHandler

def run():
    pygame.init()
    # start game clock
    clock = pygame.time.Clock()

    # define event loop tick (faster than gui update)
    event_loop_tick = configuration.fps * configuration.event_loop_multiplier

    # set up scene
    scenemodule.SceneManager.load_scene('pallet-town')
    _scene = scenemodule.SceneManager.scene

    # construct GUI
    screen_size = configuration.screen_width, configuration.screen_height
    gui = gui.Gui(screen_size, configuration.layer_limit)
    gui.set_focus('player')
    _scene.start()

    # GAME LOOP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    total_frames = 0
    while True:
        pygame.event.pump()

        # handle continuous input
        InputHandler.event_tick()

        # this code is not called as often as the outer loop
        if total_frames % (event_loop_tick / configuration.fps) == 0:
            gui.draw()

            # handle once-per-frame input
            InputHandler.gui_tick()

            _scene.update()

            # clear input stream
            InputHandler.clear()

        clock.tick(event_loop_tick)
        total_frames += 1
