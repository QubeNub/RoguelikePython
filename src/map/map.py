from tile import Tile


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [[]]
        self.entities = [[]]

    def init(self):
        self.tiles = [[Tile(' ', False, True) in range(self.width)] in range(self.height)]
        self.entities = [[None in range(self.width)] in range(self.height)]