from Component import Component

class InputComponent(Component):
    def __init(self, entity):
        Component.__init__(self, entity, 'input')
        self.continuous_input = None
        self.event_input = None

    def update(self):
        Component.update(self)

