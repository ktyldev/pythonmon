import pygame

from Configuration import Configuration
from Logger import Logger

class Tile(pygame.Rect):
	def __init__(self, id, x, y, width, height):
		self.id = id
		self.x = x
		self.y = y
		self.size = (width, height)

class TileManager():
	NORTH = (0, -1)
	EAST = (1, 0)
	SOUTH = (0, 1)
	WEST = (-1, 0)

	_tile_size = Configuration.tile_size

	map_width = 0
	map_height = 0

	List = []

	@staticmethod
	def pixel_to_tile(vector):
		return (vector[0] / TileManager._tile_size, vector[1] / TileManager._tile_size)
	
	@staticmethod
	def tile_to_pixel(x, y):
		return (x * TileManager._tile_size, y * TileManager._tile_size)

	@staticmethod
	def id_from_position(vector):
		return vector[0] * TileManager.map_width + vector[1]

	@staticmethod 
	def position_from_id(id):
		x = id % TileManager.map_width
		y = id / TileManager.map_height
		return (x, y)

	@staticmethod
	def load_tiles(rect):
		tile_size = TileManager._tile_size

		TileManager.map_width = rect.width / tile_size
		TileManager.map_height = rect.height / tile_size

		if not rect.width % tile_size == 0 or not rect.width % tile_size == 0:
			raise Exception('rect is of incorrect size')

		Logger.log('Map Height: ' + str(TileManager.map_height) + ' Map Width: ' + str(TileManager.map_width))

		tile_count = 0
		for h in range(0, TileManager.map_height):
			for w in range(0, TileManager.map_width):
				tile = Tile(tile_count, w * tile_size, h * tile_size, tile_size, tile_size)
				TileManager.List.append(tile)
				tile_count += 1

		Logger.log('Tiles created: ' + str(tile_count))

	@staticmethod
	def get_tile_neighbour_id(tile_id, tile_direction):

		tile_size = TileManager._tile_size
		
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
		
		return -1
