from Component import Component

from Logger import Logger
from Tile import *
from Helpers import Helpers

class MovementComponent(Component):
	def __init__(self, entity, movement_speed):
		Component.__init__(self, entity, 'movement')

		self.position = TileManager.pixel_to_tile((entity.x, entity.y))

		self.movement_speed = movement_speed
		self.direction_vector = None
		self.target_pos = None
	
	def set_target(self, direction):
		next_tile_pos = Helpers.add_vectors(self.position, direction)

		if next_tile_pos == Tile.INVALID_TILE_POSITION:
			Logger.log('can\'t go that way!')
			return

		self.target_pos = next_tile_pos
		self.direction_vector = direction
		
	def remove_target(self):
		self.target_pos = None

	def move(self):
		pixel_pos = (self.entity.x, self.entity.y)

		if TileManager.pixel_to_tile(pixel_pos) == self.target_pos:
			self.remove_target()
			return

		self.entity.x += self.direction_vector[0] * self.movement_speed
		self.entity.y += self.direction_vector[1] * self.movement_speed

	def update(self):
		Component.update(self)
		if self.target_pos:
			self.move()