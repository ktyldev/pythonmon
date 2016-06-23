import JsonManager

from Configuration import *

from Gui import Gui
from Entity import *
from Component import *

Logger.log('Program started')

# SETUP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pygame.init()

clock = pygame.time.Clock()

gui_tick = Configuration.fps
event_loop_tick = gui_tick * Configuration.event_loop_multiplier

ticks = 0
gui_ticks = 0

# Initialise entities
overworld = Entity('background')
player = Entity('player', (160, 160))

# Initialise components
overworld.components.append(
    GraphicsComponent(
        overworld,
        Constants.BACKGROUND_FOLDER_PATH + 'pallet-town.png',
        0)
)
overworld.components.append(
    TileMapComponent(
        overworld,
        Configuration.tile_size,
        JsonManager.get_data(Constants.MAP_DATA_FOLDER_PATH + 'pallet-town-map-data.json'),
        Configuration.property_names
    )
)

player.components.append(
    GraphicsComponent(
        player,
        Constants.PLAYER_SPRITE_FOLDER_PATH + 'player.png',
        Constants.PLAYER_LAYER,
        Constants.PLAYER_SPRITE_OFFSET)
)
player.components.append(PlayerInputComponent(player))
player.components.append(
    MovementComponent(
        player,
        2,
        player.get_component('player input'),
        overworld.get_component('tile map')
    )
)

Gui.set_focus(player.get_component('graphics'))

# start components

for entity in Entity.List:
    entity.start()

# LOOP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

while True:
    pygame.event.pump()

    InputHandler.event_tick()

    if ticks % (event_loop_tick / gui_tick) == 0:
        Gui.draw()

        InputHandler.gui_tick()

        for entity in Entity.List:
            entity.update()

        InputHandler.clear()
        gui_ticks += 1

    clock.tick(event_loop_tick)
    ticks += 1
