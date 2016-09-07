import model.tile as tile_model
from controller.component import Component
from util import configuration
from view.entity import Entity


class TileMapComponent(Component):
    def __init__(self):
        super().__init__()
        self.tag = 'tile map'
        self.map_name = ''
        self.map = None
        self.tile_size = configuration.tile_size

    def start(self):
        self.map = tile_model.Map.from_data(self.map_name)

        for tile_id in range(0, self.map.tile_count()):
            tile_coord = self.map.id_to_coord(tile_id)

            entity = Entity(str.format('tile[{0}]', tile_id), tile_coord)
            self.scene.add_entity(entity)

        super().start()

    def load_data(self, data_array):
        self.map_name = data_array[0]

    def get_tile_type(self, position):
        return self.map.get_tile_type(position)

    def in_bounds(self, tile_position):
        return self.map.in_bounds(tile_position)
