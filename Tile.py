import pygame

from Configuration import Configuration
from Entity import Entity
from Logger import Logger

class Tile(pygame.Rect):
	def __init__(self, id, x, y, width, height):
		self.id = id
		self.x = x
		self.y = y
		self.size = (width, height)

	@staticmethod
	def invalid_tile():
		return Tile(-1)

class TileManager():
	NORTH = 0
	EAST = 1
	SOUTH = 2
	WEST = 3 

	_tile_size = Configuration.tile_size

	map_width = 0
	map_height = 0

	List = []

	@staticmethod
	def load_tiles():
		tile_size = TileManager._tile_size

		background_entity = Entity.find('background')
		background_rect = background_entity.surface.get_rect()

		TileManager.map_width = background_rect.width / tile_size
		TileManager.map_height = background_rect.height / tile_size

		if not background_rect.width % tile_size == 0 or not background_rect.width % tile_size == 0:
			raise Exception('map is of incorrect size')

		Logger.log('Map Height: ' + str(TileManager.map_height) + ' Map Width: ' + str(TileManager.map_width))

		tile_count = 0
		for h in range(0, TileManager.map_height):
			for w in range(0, TileManager.map_width):
				tile = Tile(tile_count, w * tile_size, h * tile_size, tile_size, tile_size)
				TileManager.List.append(tile)
				tile_count += 1

		Logger.log('Tiles created: ' + str(tile_count))

	@staticmethod
	def get_tile_neighbour(tile_id, tile_direction):

		size = TileManager._tile_size
		
		if tile_direction == TileManager.NORTH:
			if tile_id - _tile_size >= 0:
				return tile_id - tile_size
		
		elif tile_direction == TileManager.EAST:
			if (tile_id + 1) % tile_size != 0:
				return tile_id + 1
				
		elif tile_direction == TileManager.SOUTH:
			if tile_id + _tile_size <= TileManager.List.count:
				return tile_id + tile_size
		
		elif tile_direction == TileManager.WEST:
			if tile_id % tile_size != 0:
				return tile_id - 1
		
		return Tile.invalid_tile()
