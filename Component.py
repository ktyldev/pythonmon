class Component:
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

    def update(self):
        return