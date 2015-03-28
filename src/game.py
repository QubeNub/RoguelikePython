from engine import Engine


class Game:
    def __init__(self):
        self.engine = Engine()
        self.engine.start()

game = Game()

