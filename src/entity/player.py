from entity import Entity


class Player(Entity):
    def __init__(self, move_component):
        super(self).__init__(self, move_component)