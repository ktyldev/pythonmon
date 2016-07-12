import pygame
import Gui
import Configuration
import SceneModule
from Input import InputHandler

def run():
    pygame.init()
    # start game clock
    clock = pygame.time.Clock()

    # construct GUI
    screen_size = Configuration.screen_width, Configuration.screen_height
    gui = Gui.Gui(screen_size, Configuration.layer_limit)

    # define event loop tick (faster than gui update)
    event_loop_tick = Configuration.fps * Configuration.event_loop_multiplier

    # set up scene
    SceneModule.SceneManager.load_scene('pallet-town')
    _scene = SceneModule.SceneManager.scene

    # centre player on the screen
    gui.set_focus('player')
    _scene.start()

    # GAME LOOP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    total_frames = 0
    while True:
        pygame.event.pump()

        # handle continuous input
        InputHandler.event_tick()

        # this code is not called as often as the outer loop
        if total_frames % (event_loop_tick / Configuration.fps) == 0:
            gui.draw()

            # handle once-per-frame input
            InputHandler.gui_tick()

            # update components
            _scene.update()

            # clear input stream
            InputHandler.clear()

        clock.tick(event_loop_tick)
        total_frames += 1
