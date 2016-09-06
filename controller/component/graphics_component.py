import pygame
from controller.component import Component


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