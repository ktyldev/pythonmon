from util import configuration


class Entity:
    """
    representation for objects in the game world, container for components
    """

    def __init__(self, name, position=(0, 0)):
        self.name = name
        self.x = position[0] * configuration.tile_size
        self.y = position[1] * configuration.tile_size
        self.child_entities = []
        self.components = []
        self.direction = None

    def get_component(self, component_type):
        """
        return component of given type
        :param component_type: type of component as string eg 'graphics'
        :return:
        """
        for component in self.components:
            if component.tag == component_type:
                return component

    def add_component(self, component):
        component.entity = self
        self.components.append(component)

    def start(self):
        """
        called at start of scene
        :return:
        """
        if len(self.components) > 0:
            for component in self.components:
                if component.enabled and not component.started:
                    component.start()

    def update(self):
        """
        called once per tick
        :return:
        """
        for component in self.components:
            if component.enabled:
                component.update()

    def is_started(self):
        for component in self.components:
            if not component.started:
                return False
        return True
