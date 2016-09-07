from util import jsonmanager


class Map:
    current = None

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
            tile_map.add_tile(tile_data['Type'])

        return tile_map

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tile_array = []
        Map.current = self

    def id_to_coord(self, tile_id):
        y = tile_id // self.width
        x = tile_id % self.width
        return x, y

    def coord_to_id(self, coord):
        return coord[1] * self.width + coord[0]

    def add_tile(self, tile_type):
        self.tile_array.append(tile_type)

    def in_bounds(self, coord):
        x = coord[0]
        y = coord[1]

        valid_x_range = range(0, self.width)
        valid_y_range = range(0, self.height)

        return x in valid_x_range and y in valid_y_range

    def get_tile_type(self, pos):
        if not self.in_bounds(pos):
            return None

        tile_id = self.coord_to_id(pos)
        return self.tile_array[tile_id]

    def tile_count(self):
        return len(self.tile_array)

    def get_tiles(self):
        return self.tile_array
