from controller.component import Component


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
