import pygame

from Logger import Logger
from Constants import Constants

class Entity:

	List = []

	@staticmethod
	def find(name):
		for entity in Entity.List:
			if entity.name == name:
				return entity
		return None

	def __init__(self, name, image, layer, x = 0, y = 0):
		if image == '':
			image = Constants.BLANK_IMAGE_FILE

		self.surface = pygame.image.load(image)
		self.name = name
		self.layer = layer
		self.x = x
		self.y = y
		self.child_entities = []
		self.components = []
		self.target = None

		Entity.List.append(self)

		Logger.log(self.name + ' initialised at ' + str(self.x) + ", " + str(self.y))

	def move_position(self, x, y):
		self.x += x
		self.y += y

		if self.child_entities:
			for e in self.child_entities:
				e.move_position(x, y)

	def set_position(self, x, y):
		delta_x = x - self.x
		delta_y = y - self.y
		
		move_position(delta_x, delta_y)

class Player(Entity):
	def __init__(self, image, x = 0, y = 0):
		Entity.__init__(self, Constants.PLAYER_NAME, image, Constants.PLAYER_LAYER, x, y)
			


