from system.render_system import RenderSystem
from lib import libtcodpy as libtcod


class Engine:
    def __init__(self):
        self.running = True
        self.render_system = RenderSystem()

    def stop(self):
        self.running = False

    def start(self):
        while self.running:
            self.render_system.update()
            key = libtcod.console_wait_for_keypress(True)

            if key.vk == libtcod.KEY_ESCAPE:
                break

