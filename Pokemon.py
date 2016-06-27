from Configuration import *

from Gui import Gui
from Component import *

Logger.log('Program started')

# SETUP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pygame.init()

clock = pygame.time.Clock()

gui_tick = Configuration.fps
event_loop_tick = gui_tick * Configuration.event_loop_multiplier

ticks = 0

SceneModule.SceneManager.scene_data_folder_path = Constants.SCENE_DATA_FOLDER_PATH
SceneModule.SceneManager.load_scene('pallet-town')
_scene = SceneModule.SceneManager.scene

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gui.set_focus('player')

# start components

_scene.start()

# LOOP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

while True:
    pygame.event.pump()

    InputHandler.event_tick()

    if ticks % (event_loop_tick / gui_tick) == 0:
        Gui.draw()

        InputHandler.gui_tick()

        _scene.update()

        InputHandler.clear()

    clock.tick(event_loop_tick)
    ticks += 1
