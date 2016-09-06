from util import jsonmanager, configuration, helpers


class Map:
    @staticmethod
    def from_data(map_name):
        folder = '_Resources/Data/MapData/'
        path = folder + map_name + '-map-data.json'
        tile_map_data = jsonmanager.get_data(path)

        width = tile_map_data['Width']
        height = tile_map_data['Height']

        tile_map = Map(width, height)

        tiles = tile_map_data['Tiles']

        for tile_data in tiles:
            tile_id = tile_data['Id']
            tile_type = tile_data['Type']

            tile = Tile(tile_id, tile_type)
            tile_map.add_tile(tile)

        return tile_map

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tile_list = []

    def id_to_coord(self, tile_id):
        y = tile_id // self.width
        x = tile_id % self.width
        return x, y

    def coord_to_id(self, coord):
        return coord[1] * self.width + coord[0]

    def add_tile(self, tile):
        self.tile_list.append(tile)

    def get_tile(self, coord):
        for tile in self.tile_list:
            if helpers.vector_equality(self.id_to_coord(tile.tile_id), coord):
                return tile
        return None

    def in_bounds(self, coord):
        x = coord[0]
        y = coord[1]

        valid_x_range = range(0, self.width)
        valid_y_range = range(0, self.height)

        return x in valid_x_range and y in valid_y_range


# TODO:
# since ids are sequential this data could be stored as an array
# without too much hassle
class Tile:
    def __init__(self, tile_id, tile_type):
        self.tile_id = tile_id
        self.tile_type = tile_type
