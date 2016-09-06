from controller.component import Component


class TileComponent(Component):
    def __init__(self, tile):
        super().__init__()
        self.tile = tile
