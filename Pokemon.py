import pygame, ConfigParser

from Gui import Gui
from Logger import Logger
from Constants import Constants
from Configuration import Configuration

from Entity import *
from Input import *
from Tile import TileManager

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

		# Initialising test entities
		overworld = Entity('background', Constants.BACKGROUND_FOLDER_PATH + 'pallet-town.png', 0)
		player = Player(Constants.PLAYER_SPRITE_FOLDER_PATH + 'player.png', 160, 160)
		above_player = Player(Constants.PLAYER_SPRITE_FOLDER_PATH + 'player.png', 160, 144)
		below_player = Player(Constants.PLAYER_SPRITE_FOLDER_PATH + 'player.png', 160, 176)

		# Initialise tile engine
		TileManager.load_tiles()
# LOOP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		while True:
			pygame.event.pump()

			event_data = InputHandler.get_event_data()
			if event_data:
				Logger.log(str(event_data.action) + ' ' + event_data.pressed)

			if ticks % (event_loop_tick / gui_tick) == 0:
				Gui.draw()
				#Logger.log(str(ticks) + " | " + str(gui_ticks))

				gui_ticks += 1

			clock.tick(event_loop_tick)
			ticks += 1

# START ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Program.run()