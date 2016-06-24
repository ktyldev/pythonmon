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

# overworld graphics component
overworld.add_component(GraphicsComponent())
overworld_graphics = overworld.get_component('graphics')
overworld_graphics.image = Constants.BACKGROUND_FOLDER_PATH + 'pallet-town.png'
overworld_graphics.layer = 0

# overworld tile map
overworld.add_component(TileMapComponent())
overworld_tile_map = overworld.get_component('tile map')
overworld_tile_map.tile_size = Configuration.tile_size
overworld.tile_map_data = JsonManager.get_data(Constants.MAP_DATA_FOLDER_PATH + 'pallet-town-map-data.json')

# player graphics component
player.add_component(GraphicsComponent())
player_graphics = player.get_component('graphics')
player_graphics.offset = Constants.PLAYER_SPRITE_OFFSET
player_graphics.layer = Constants.PLAYER_LAYER
player_graphics.image = Constants.PLAYER_SPRITE_FOLDER_PATH + 'player.png'

# player input component
player.add_component(PlayerInputComponent())

# player movement component
player.add_component(MovementComponent())
player_movement = player.get_component('movement')
player_movement.tile_map_component = overworld.get_component('tile map')
player_movement.input_component = player.get_component('player input')
player_movement.movement_speed = 2

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
