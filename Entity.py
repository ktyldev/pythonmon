from Logger import Logger


class Entity:
    """
    representation for objects in the game world, container for components
    """
    List = []

    def __init__(self, name, position=(0, 0)):
        self.name = name
        self.x = position[0]
        self.y = position[1]
        self.child_entities = []
        self.components = []

        Entity.List.append(self)

        Logger.log(self.name + ' initialised at ' + str(self.x) + ", " + str(self.y))

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
        for component in self.components:
            if component.enabled:
                component.start()

    def update(self):
        """
        called once per tick
        :return:
        """
        for component in self.components:
            if component.enabled:
                component.update()
