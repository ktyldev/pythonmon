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

# SETUP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		Logger._state = True
		Logger.log('Program started')
		Gui.log_drawing = True

		TileManager._tile_size = Configuration.tile_size

		pygame.init()

		#Configuration.load()

		Program.prepare_gui()

		clock = pygame.time.Clock()

		#fps is not configurable as it is not likely to change
		gui_tick = Configuration.fps
		event_loop_tick = gui_tick * Configuration.event_loop_multiplier
		ticks = 0
		gui_ticks = 0

		# Initialising test entities
		overworld = Entity('overworld', Constants.BACKGROUND_FOLDER_PATH + 'pallet-town.png', 0)
		player = Player(Constants.PLAYER_SPRITE_FOLDER_PATH + 'player.png', 10, 10)

# LOOP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		while True:
			pygame.event.pump()

			event_data = InputHandler.get_event_data()
			if event_data:
				Logger.log(str(event_data.action) + ' ' + event_data.pressed)

			# gui loop called every 5 event loops
			if ticks % (event_loop_tick / gui_tick) == 0:
				Gui.draw()
				#Logger.log(str(ticks) + " | " + str(gui_ticks))

				gui_ticks += 1

			clock.tick(event_loop_tick)
			ticks += 1

	@staticmethod
	def prepare_gui():

		screen_width = Configuration.screen_width
		screen_height = Configuration.screen_height
		layer_limit = Configuration.layer_limit
		
		Gui.set_screen_size(screen_width, screen_height)
		Gui.set_layer_limit(layer_limit)

# START ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Program.run()