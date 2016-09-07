from util import helpers, debug, configuration
from controller.component import Component


class MovementComponent(Component):
    """
    Handles tile-based movement
    """

    def __init__(self):
        super().__init__()
        self.tag = 'movement'
        self.tile_map_component = None
        self.input_component = None
        self.movement_speed = 0
        self.position = 0, 0
        self.direction = None
        self.target_pos = None

    def start(self):
        super().start()

        overworld = self.scene.find_entity('overworld')
        self.tile_map_component = overworld.get_component('tile map')

        player = self.scene.find_entity('player')
        self.input_component = player.get_component('player input')
        self.position = self.entity.get_world_pos()

    def update(self):
        super().update()

        current_input = self.input_component.continuous_input

        if self.target_pos:
            self.move()
        elif current_input != 'none':
            self.set_target(current_input)

    def load_data(self, data_array):
        self.movement_speed = data_array[0]

    def set_target(self, direction):
        """
        sets target to neighbouring tile specified by direction
        :param direction: target direction
        :return:
        """
        debug.log(direction)
        self.entity.direction = direction

        direction_vector = helpers.direction_to_direction_vector(direction)
        next_tile_pos = helpers.add_vectors(self.position, direction_vector)

        if not self.tile_map_component.in_bounds(next_tile_pos):
            debug.log('can\'t go that way!')
            return

        next_tile_type = self.tile_map_component.get_tile_type(next_tile_pos)
        if next_tile_type == 'collision':
            return

        if not helpers.vector_equality(next_tile_pos, self.position):
            self.target_pos = next_tile_pos

    def move(self):
        """
        move towards target based on movement speed
        :return:
        """
        if self.target_reached():
            self.position = self.target_pos
            self.target_pos = None
        else:
            direction_vector = helpers.direction_to_direction_vector(self.entity.direction)

            self.entity.x += direction_vector[0] * self.movement_speed
            self.entity.y += direction_vector[1] * self.movement_speed

    def target_reached(self):
        own_pixel_pos = self.entity.x, self.entity.y
        target_pixel_pos = helpers.multiply_vector(self.target_pos, configuration.tile_size)
        result = helpers.vector_equality(own_pixel_pos, target_pixel_pos)
        debug.log('[{0}]-[{1}]: {2}'.format(own_pixel_pos, target_pixel_pos, result))
        return result
