from core.input import *
from controller import entity as ent
from util import logger, configuration, helpers
import model.tile


# COMPONENT USAGE
#
#   This is where all game logic is defined. Components should only update themselves and the entity they are attached
#   to. On rare occasions it may be necessary to access other components from inside a component's update method. This
#   should be achieved via ```self.scene.find_entity(%entity_name%).get_component(%component_name%)```.
#
#   Components have parameterless constructors, two overridable parameterless methods and one overridable method with a
#   single parameter.
#
#   Component()
#
#   Every component should have a parameterless constructor defined.
#
#   component.update()
#
#   This method will be called once per tick. It is used to update the state of the Component and the entity to which
#   the component is attached.
#
#   component.start()
#
#   This method is called once at the start of the scene. It is used to prepare the state of the component using data
#   that is only available at runtime.
#
#   component.load_data(data)
#
#   This method is called before the start of the scene. It is used to load data from the scene JSON file. The data is
#   an array which can be used with index arguments to assign data to class members.

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

    def __init__(self):
        self.scene = None
        self.enabled = True
        self.tag = ''
        self.entity = None
        self.started = False
        Component.List.append(self)

    def start(self):
        """
        called at the start of the scene
        :return:
        """
        self.started = True
        return

    def update(self):
        """
        called once per tick
        :return:
        """
        return

    def load_data(self, data_array):
        """
        assign data to a class instance before starting scene
        :param data_array: an array of data to initialise the component with
        :return:
        """
        return


class GraphicsComponent(Component):
    """
    renders an image on the entity's position
    """
    List = []

    def __init__(self):
        super().__init__()
        self.tag = 'graphics'
        self.offset = 0, 0
        self.layer = 0
        self.image = None

        self.draw_x = 0
        self.draw_y = 0
        self.surface = None

        GraphicsComponent.List.append(self)

    def start(self):
        super().start()
        self.surface = pygame.image.load(self.image)
        self.draw_x = self.entity.x + self.offset[0]
        self.draw_y = self.entity.y + self.offset[1]

    def update(self):
        super().update()
        self.draw_x = self.entity.x + self.offset[0]
        self.draw_y = self.entity.y + self.offset[1]

    def load_data(self, data_array):
        self.image = data_array[0]
        self.layer = data_array[1]
        self.offset = data_array[2]


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

        self.position = self.tile_map_component.pixel_to_tile((self.entity.x, self.entity.y))

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
        next_tile_pos = int(next_tile_pos[0]), int(next_tile_pos[1])

        next_tile = self.tile_map_component.get_tile(next_tile_pos)

        if next_tile.tile_type == 'collision':
            return

        if not self.tile_map_component.in_bounds(next_tile_pos):
            logger.log('can\'t go that way!')
            return

        self.target_pos = next_tile_pos

    def move(self):
        """
        move towards target based on movement speed
        :return:
        """
        own_pixel_pos = (self.entity.x, self.entity.y)
        target_pixel_pos = self.tile_map_component.tile_to_pixel(self.target_pos)

        # You have reached your destination

        target_reached = helpers.vector_equality(own_pixel_pos, target_pixel_pos)

        if target_reached:
            self.position = self.target_pos
            self.target_pos = None

            direction = self.input_component.continuous_input
            if direction:
                self.set_target(direction)
        else:
            direction_vector = helpers.direction_to_direction_vector(self.player.direction)

            self.entity.x += direction_vector[0] * self.movement_speed
            self.entity.y += direction_vector[1] * self.movement_speed


class InputComponent(Component):
    """
    generic base class for providing input to an entity
    """
    def __init__(self):
        super().__init__()
        self.tag = 'input'
        self.continuous_input = None
        self.event_input = None

    def update(self):
        super().update()

    def load_data(self, data_array):
        return


class PlayerInputComponent(InputComponent):
    """
    receives input from InputHandler
    """
    def __init__(self):
        super().__init__()
        self.tag = 'player input'

    def update(self):
        super().update()

        self.event_input = self.scene.event_input
        self.continuous_input = self.scene.cont_input


class TileMapComponent(Component):
    def __init__(self):
        super().__init__()
        self.tag = 'tile map'
        self.map_name = ''
        self.map = None
        self.tile_size = configuration.tile_size

    def start(self):
        self.map = model.tile.Map.from_data(self.map_name)
        for tile in self.map.tile_list:
            # grid ref on tile map
            tile_coord = self.id_to_coordinate(tile.tile_id)
            # pixel position
            tile_position = self.tile_to_pixel(tile_coord)
            entity = ent.Entity('tile ' + str(tile.tile_id), tile_position)
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


class TileComponent(Component):
    def __init__(self, tile):
        super().__init__()
        self.tile = tile
