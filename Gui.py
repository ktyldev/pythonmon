import pygame

from Logger import Logger
from Constants import Constants
from Entity import Entity

class Gui:
	_layer_limit = 0
	log_drawing = False	
	_screen = pygame.display.set_mode((0, 0))
	
	Logger.log('Gui initialised')
	
	@staticmethod
	def set_screen_size(width, height):
		Gui._screen = pygame.display.set_mode((width, height))

	@staticmethod
	def set_layer_limit(layer_limit):
		Gui._layer_limit = layer_limit

	@staticmethod
	def draw():

		# clear the screen
		Gui._screen.fill(Constants.BLACK)

		entities_to_draw = []

		for layer in range(0, Gui._layer_limit):
			
			for entity in Entity.List:
				if entity.layer == layer:
					entities_to_draw.append(entity)
			
			for entity in entities_to_draw:
				Gui._screen.blit(entity.surface, (entity.x, entity.y))
				if Gui.log_drawing:
					Logger.log('Drawing entity ' + entity.name + ' on layer ' + str(layer))
				
			entities_to_draw = []	

		# update the display
		pygame.display.flip()


