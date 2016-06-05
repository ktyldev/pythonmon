import pygame

from Logger import Logger
from Constants import Constants
from Entity import Entity
from Configuration import Configuration

from Tile import *

class Gui:
	_layer_limit = Configuration.layer_limit
	_log_drawing = Configuration.log_gui
	_screen_width = Configuration.screen_width
	_screen_height = Configuration.screen_height
	_screen = pygame.display.set_mode((_screen_width, _screen_height))
	_draw_tiles = Configuration.draw_tiles
	
	@staticmethod
	def draw():

		# clear the screen
		Gui._screen.fill(Constants.BLACK)

		entities_to_draw = []

		for layer in range(0, Gui._layer_limit):
			
			for entity in Entity.List:
				if entity.layer == layer:
					entities_to_draw.append(entity)
			
			if Gui._draw_tiles:
				for tile in TileManager.List:
					pygame.draw.rect(Gui._screen, [255, 0, 0], tile)


			for entity in entities_to_draw:
				Gui._screen.blit(entity.surface, (entity.x, entity.y))
				if Gui._log_drawing:
					Logger.log('Drawing entity ' + entity.name + ' on layer ' + str(layer))

			entities_to_draw = []	

		# update the display
		pygame.display.flip()


