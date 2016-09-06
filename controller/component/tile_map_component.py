import model.tile as tile_model

from controller.component import Component
from controller.component.tile_component import TileComponent

from controller.entity import Entity
from util import configuration


class TileMapComponent(Component):
    def __init__(self):
        super().__init__()
        self.tag = 'tile map'
        self.map_name = ''
        self.map = None
        self.tile_size = configuration.tile_size

    def start(self):
        self.map = tile_model.Map.from_data(self.map_name)
        for tile in self.map.tile_list:
            # grid ref on tile map
            tile_coord = self.id_to_coordinate(tile.tile_id)
            # pixel position
            tile_position = self.tile_to_pixel(tile_coord)
            entity = Entity('tile ' + str(tile.tile_id), tile_position)
            entity.add_component(TileComponent(tile))
            self.scene.add_entity(entity)
        super().start()

    def load_data(self, data_array):
        self.map_name = data_array[0]

    def id_to_coordinate(self, tile_id):
        return self.map.id_to_coord(tile_id)

    def coordinate_to_id(self, coordinate):
        return self.map.coord_to_id(coordinate)

    def get_tile(self, position):
        return self.map.get_tile(position)

    def in_bounds(self, tile_position):
        return self.map.in_bounds(tile_position)

    def pixel_to_tile(self, vector):
        return vector[0] / self.tile_size, vector[1] / self.tile_size

    def tile_to_pixel(self, vector):
        return vector[0] * self.tile_size, vector[1] * self.tile_size
