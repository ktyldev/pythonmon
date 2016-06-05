from Tile import *
from Constants import Constants
from Logger import Logger

class Component:
	def __init__(self, entity):
		self.entity = entity

	def update(self):
		return

class MovementComponent(Component):
	def __init__(self, entity, tile, movement_speed):
		Component.__init__(self, entity)
		self.tile = tile
		self.movement_speed = movement_speed

		self.direction_vector = None
		self.target = None
	
	def set_target(self, direction):
		next_tile = TileManager.get_tile_neighbour(self.tile.id, direction)
		if next_tile == Tile.invalid_tile().id:
			Logger.log('can\t go that way!')
			return

		self.target = next_tile
		
	def remove_target(self):
		self.target = None

	def move(self):
		self.entity.x += self.direction_vector[0] * self.movement_speed
		self.entity.y += self.direction_vector[1] * self.movement_speed

	def update(self):
		Component.update(self)
		if target:
			move()