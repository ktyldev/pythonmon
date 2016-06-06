import pygame, ConfigParser

from Gui import Gui
from Logger import Logger
from Constants import Constants
from Configuration import Configuration

from Entity import *
from Input import *
from Tile import TileManager

from Component import *

class Program:

	@staticmethod
	def run():
		Logger.log('Program started')

# SETUP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		pygame.init()

		clock = pygame.time.Clock()

		gui_tick = Configuration.fps
		event_loop_tick = gui_tick * Configuration.event_loop_multiplier
		
		ticks = 0
		gui_ticks = 0


		# Initialise map
		overworld = Entity('background', Constants.BACKGROUND_FOLDER_PATH + 'pallet-town.png', 0)

		# Initialise tile engine
		TileManager.load_tiles(overworld.surface.get_rect())

		# Initialise game objects
		player = Player(Constants.PLAYER_SPRITE_FOLDER_PATH + 'player.png', 160, 160)
		player.components.append(MovementComponent(player, 1))
# LOOP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		while True:
			pygame.event.pump()

			event_data = InputHandler.get_event_data()
			if event_data:
				Logger.log(str(event_data.key) + ' ' + str(event_data.state))

			continuous_data = InputHandler.get_continuous_data()
			if continuous_data:
				Logger.log(str(continuous_data.action_key) + ' ' + str(continuous_data.movement_key))

			if ticks % (event_loop_tick / gui_tick) == 0:
				Gui.draw()
				#Logger.log(str(ticks) + " | " + str(gui_ticks))

				for entity in Entity.List:
					entity.update()

				gui_ticks += 1

			clock.tick(event_loop_tick)
			ticks += 1

# START ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Program.run()