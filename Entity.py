from Logger import Logger


class Entity:
    """
    representation for objects in the game world, container for components
    """
    List = []

    @staticmethod
    def find(name):
        """
        returns entity based on name
        :param name: name of entity
        :return:
        """
        for entity in Entity.List:
            if entity.name == name:
                return entity
        return None

    def __init__(self, name, position = (0, 0)):
        self.name = name
        self.x = position[0]
        self.y = position[1]
        self.child_entities = []
        self.components = []

        Entity.List.append(self)

        Logger.log(self.name + ' initialised at ' + str(self.x) + ", " + str(self.y))

    def get_component(self, component_tag):
        for component in self.components:
            if component.tag == component_tag:
                return component

    def update(self):
        for component in self.components:
            if component.enabled:
                component.update()
