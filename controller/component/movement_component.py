from util import helpers, logger, configuration
from controller.component import Component


class MovementComponent(Component):
    """
    Handles tile-based movement
    """

    def __init__(self):
        super().__init__()
        self.tag = 'movement'
        self.position = 0, 0
        self.tile_map_component = None
        self.input_component = None
        self.movement_speed = 0

        self.direction = None
        self.target_pos = None
        self.player = None

    def start(self):
        super().start()
        overworld = self.scene.find_entity('overworld')
        self.tile_map_component = overworld.get_component('tile map')
        self.player = self.scene.find_entity('player')
        self.input_component = self.player.get_component('player input')

    def update(self):
        super().update()

        current_input = self.input_component.continuous_input
        if current_input:
            self.move_command(current_input)

        if self.target_pos:
            self.move()

    def load_data(self, data_array):
        self.movement_speed = data_array[0]

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
        self.player.direction = direction

        direction_vector = helpers.direction_to_direction_vector(direction)

        next_tile_pos = helpers.add_vectors(self.position, direction_vector)

        if not self.tile_map_component.in_bounds(next_tile_pos):
            logger.log('can\'t go that way!')
            return

        next_tile_type = self.tile_map_component.get_tile_type(next_tile_pos)
        if next_tile_type == 'collision':
            return

        self.target_pos = next_tile_pos

    def move(self):
        """
        move towards target based on movement speed
        :return:
        """
        if self.target_reached():
            self.position = self.target_pos
            self.target_pos = None

            direction = self.input_component.continuous_input
            if direction:
                self.set_target(direction)
        else:
            direction_vector = helpers.direction_to_direction_vector(self.player.direction)

            self.entity.x += direction_vector[0] * self.movement_speed
            self.entity.y += direction_vector[1] * self.movement_speed

    def target_reached(self):
        own_pixel_pos = self.entity.x, self.entity.y
        target_pixel_pos = helpers.multiply_vector(self.target_pos, configuration.tile_size)

        return helpers.vector_equality(own_pixel_pos, target_pixel_pos)
