from Component import Component
from Tile import TileManager

class GraphicsComponent(Component):
	
	List = []
	
	def __init__(self, entity, image, layer):
		Component.__init__(self, entity, 'graphics')
		self.draw_x = 0
		self.draw_y = 0
		self.layer = layer
		self.surface = pygame.image.load(image)
		GraphicsComponent.List.append(self)

	def update(self):
		Component.update(self)
		self.draw_x = self.entity.x
		self.draw_y = self.entity.y - (self.surface.rect.height - TileManager._tile_size)