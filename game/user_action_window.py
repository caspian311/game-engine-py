# pylint: disable=R0801
from cursed import CursedWindow

from game.data import DATA, GameState

class UserActionsWindow(CursedWindow):
    X, Y = (0, DATA.window["height"] - 10)
    WIDTH, HEIGHT = (int(DATA.window["width"] / 2) - 1, 10)
    BORDERED = True

    @classmethod
    def update(cls):
        if DATA.state.run_state == GameState.QUITTING:
            cls.trigger('quit')

        cls._clear_screen(cls.WIDTH, cls.HEIGHT)

        if DATA.state.run_state == GameState.IN_BATTLE:
            cls.addstr("Choose your action:", 1, 2)
            cls.addstr("A: ATTACK", 1, 3)
            cls.addstr("M: MAGIC", 1, 4)
            cls.addstr("D: DEFEND", 1, 5)
            cls.addstr("H: HEAL", 1, 6)

            k = cls.getch()
            if k == ord('a'):
                DATA.user.set_turn('a')
            elif k == ord('m'):
                DATA.user.set_turn('m')
            elif k == ord('d'):
                DATA.user.set_turn('d')
            elif k == ord('h'):
                DATA.user.set_turn('h')

        cls.sleep(.1)
        cls.refresh()

    @classmethod
    def _clear_screen(cls, width, height):
        line = "".join([" " for x in range(0, width-3)])
        for y in range(1, height-2):
            cls.addstr(line, 1, y)
