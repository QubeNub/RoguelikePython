import lib.libtcodpy as libtcod


class RenderSystem:

    def __init__(self):
        self.SCREEN_WIDTH = 80
        self.SCREEN_HEIGHT = 50
        libtcod.console_set_custom_font('../terminal.png')
        libtcod.console_init_root(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, 'python/libtcod tutorial', False)

    def update(self):
        libtcod.console_set_default_foreground(0, libtcod.white)
        libtcod.console_put_char(0, 20, 20, '@', libtcod.BKGND_NONE)

        libtcod.console_flush()

        libtcod.console_put_char(0, 20, 20, ' ', libtcod.BKGND_NONE)