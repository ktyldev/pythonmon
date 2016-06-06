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
player = Entity('player', 160, 160)

# Initialise components
overworld.components.append(GraphicsComponent(overworld, Constants.BACKGROUND_FOLDER_PATH + 'pallet-town.png', 0))

player.components.append(GraphicsComponent(player, Constants.PLAYER_SPRITE_FOLDER_PATH + 'player.png', Constants.PLAYER_LAYER))
player.components.append(MovementComponent(player, 2))
player.components.append(PlayerInputComponent(player, player.get_component('movement')))

# Initialise tile engine
TileManager.load_tiles(overworld.get_component('graphics').surface.get_rect())

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
