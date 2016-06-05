import pygame

class Tile(pygame.Rect):
	def __init__(self, id):
		self.id = id

class TileManager():

	_tile_size = 0

	List = []

	@staticmethod
	def create_tiles():
		return
