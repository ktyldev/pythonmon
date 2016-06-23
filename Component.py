from Helpers import Helpers
from Logger import Logger
from Input import *


class Component:
    """
    generic base class for defining entity behaviour
    """
    List = []

    @staticmethod
    def find(tag):
        for component in Component.List:
            if component.tag == tag:
                return component
        return None

    def __init__(self, entity, tag):
        self.entity = entity
        self.enabled = True
        self.tag = tag
        Component.List.append(self)

    def start(self):
        """
        called at the start of the scene
        :return:
        """
        return

    def update(self):
        """
        called once per tick
        :return:
        """
        return


class GraphicsComponent(Component):
    """
    renders an image on the entity's position
    """
    List = []

    def __init__(self, entity, image, layer, offset=(0, 0)):
        """

        :param entity:
        :param image: path to image to use
        :param layer: gui layer to draw image on
        :param offset: fine tune image position against entity position
        """
        super().__init__(entity, 'graphics')

        self.draw_x = 0
        self.draw_y = 0

        self.offset = offset

        self.layer = layer
        self.surface = pygame.image.load(image)
        GraphicsComponent.List.append(self)

    def update(self):
        super().update()
        self.draw_x = self.entity.x + self.offset[0]
        self.draw_y = self.entity.y + self.offset[1]


class MovementComponent(Component):
    """
    Handles tile-based movement
    """

    def __init__(self, entity, movement_speed, input_component, tile_map_component):
        super().__init__(entity, 'movement')

        self.position = tile_map_component.pixel_to_tile((entity.x, entity.y))

        self.tile_map_component = tile_map_component
        self.input_component = input_component
        self.movement_speed = movement_speed
        self.direction = None
        self.target_pos = None

    def move_command(self, direction):
        """
        sets target direction if no target is set
        :param direction: target direction
        :return:
        """
        if not self.target_pos:
            self.set_target(direction)

    def set_target(self, direction):
        """
        sets target to neighbouring tile specified by direction
        :param direction: target direction
        :return:
        """
        self.direction = direction

        direction_vector = Helpers.direction_to_direction_vector(direction)

        next_tile_pos = Helpers.add_vectors(self.position, direction_vector)
        next_tile_pos = int(next_tile_pos[0]), int(next_tile_pos[1])

        if self.tile_map_component.get_tile_property(next_tile_pos) == 'collision':
            return

        if not self.tile_map_component.in_bounds(next_tile_pos):
            Logger.log('can\'t go that way!')
            return

        self.target_pos = next_tile_pos

    def move(self):
        """
        move towards target based on movement speed
        :return:
        """
        pixel_pos = (self.entity.x, self.entity.y)

        # You have reached your destination

        target_reached = Helpers.vector_equality(pixel_pos, self.tile_map_component.tile_to_pixel(self.target_pos))

        if target_reached:
            self.position = self.target_pos
            self.target_pos = None

            direction = self.input_component.continuous_input
            if direction:
                self.set_target(direction)
        else:
            direction_vector = Helpers.direction_to_direction_vector(self.direction)

            self.entity.x += direction_vector[0] * self.movement_speed
            self.entity.y += direction_vector[1] * self.movement_speed

    def update(self):
        super().update()

        current_input = self.input_component.continuous_input
        if current_input:
            self.move_command(current_input)

        if self.target_pos:
            self.move()


class InputComponent(Component):
    """
    generic base class for providing input to an entity
    """
    def __init__(self, entity, tag):
        super().__init__(entity, tag)
        self.continuous_input = None
        self.event_input = None

    def update(self):
        super().update()


class PlayerInputComponent(InputComponent):
    """
    receives input from InputHandler
    """
    def __init__(self, entity):
        super().__init__(entity, 'player input')

    def update(self):
        super().update()

        self.event_input = InputHandler.current_event
        self.continuous_input = InputHandler.current_continuous


class TileMapComponent(Component):
    class Tile:
        """
        stores tile data for use by a TileMapComponent object
        """
        def __init__(self, tile_id, tile_type):
            self.tile_id = tile_id
            self.tile_type = tile_type

    def __init__(self, entity, tile_size, tile_map_data, tile_property_names):
        super().__init__(entity, 'tile map')

        self.map_width = tile_map_data['Width']
        self.map_height = tile_map_data['Height']
        self.tiles_data = tile_map_data['Tiles']

        self.tile_size = tile_size
        self.tile_property_names = tile_property_names
        self.tile_list = []

    def start(self):
        super().start()

        for tile_datum in self.tiles_data:
            tile = TileMapComponent.Tile(tile_datum['Id'], tile_datum['Type'])
            self.tile_list.append(tile)

    def id_to_coordinate(self, tile_id):
        y = tile_id // self.map_width
        x = tile_id % self.map_width

        return x, y

    def coordinate_to_id(self, coordinate):
        return coordinate[1] * self.map_width + coordinate[0]

    def get_tile(self, position):
        """
        returns tile at position.
        :param position: where to look for a tile
        :return:
        """
        for tile in self.tile_list:
            if Helpers.vector_equality(self.id_to_coordinate(tile.tile_id), position):
                return tile
        return None

    def get_tile_property(self, tile_position):
        tile = self.get_tile(tile_position)
        return tile.tile_type

    def in_bounds(self, tile_position):
        x = tile_position[0]
        y = tile_position[1]

        valid_x_range = range(0, self.map_width)
        valid_y_range = range(0, self.map_height)

        return x in valid_x_range and y in valid_y_range

    def pixel_to_tile(self, vector):
        return vector[0] / self.tile_size, vector[1] / self.tile_size

    def tile_to_pixel(self, vector):
        return vector[0] * self.tile_size, vector[1] * self.tile_size