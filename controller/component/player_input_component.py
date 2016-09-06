from controller.component import InputComponent


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
