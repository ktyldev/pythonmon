from Gui import Gui
from Component import *

Logger.log('Program started')

# SETUP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pygame.init()

# start game clock
clock = pygame.time.Clock()

event_loop_tick = Gui.frames_per_second * Configuration.event_loop_multiplier

SceneModule.SceneManager.load_scene('pallet-town')
_scene = SceneModule.SceneManager.scene

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gui.set_focus('player')
_scene.start()

# LOOP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

total_frames = 0
while True:
    pygame.event.pump()

    # handle continuous input
    InputHandler.event_tick()

    # this code is not called as often as the outer loop
    if total_frames % (event_loop_tick / Gui.frames_per_second) == 0:
        Gui.draw()

        # handle once-per-frame input
        InputHandler.gui_tick()

        # update components
        _scene.update()

        # clear input stream
        InputHandler.clear()

    clock.tick(event_loop_tick)
    total_frames += 1
