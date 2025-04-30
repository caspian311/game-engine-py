from cursed import CursedWindow

from game.commands import Commands, CommandProcessor
from game.data import DATA, GameState

class UserActionsWindow(CursedWindow):
    X, Y = (0, DATA.window["height"] - 10)
    WIDTH, HEIGHT = (int(DATA.window["width"] / 2) - 1, 10)
    BORDERED = True

    @classmethod
    def update(cls):
        if DATA.state.run_state == GameState.RUN_STATE_QUITTING:
            cls.trigger('quit')

        cls._clear_screen(cls.WIDTH, cls.HEIGHT)

        if DATA.state.in_battle:
            cls.addstr("Choose your action:", 1, 2)
            cls.addstr("A: ATTACK", 1, 3)
            cls.addstr("M: MAGIC", 1, 4)
            cls.addstr("D: DEFEND", 1, 5)
            cls.addstr("H: HEAL", 1, 6)

            k = cls.getch()
            if k == ord('a'):
                CommandProcessor.queue_command(
                        Commands.PHYSICAL_ATTACK, [DATA.user, DATA.live_npcs()[0]])
            elif k == ord('m'):
                CommandProcessor.queue_command(
                        Commands.MAGIC_ATTACK, [DATA.user, DATA.live_npcs()[0]])
            elif k == ord('d'):
                CommandProcessor.queue_command(Commands.DEFEND, [DATA.user])
            elif k == ord('h'):
                CommandProcessor.queue_command(Commands.HEAL, [DATA.user])

        cls.sleep(.1)
        cls.refresh()

    @classmethod
    def _clear_screen(cls, width, height):
        line = "".join([" " for x in range(0, width-3)])
        for y in range(1, height-2):
            cls.addstr(line, 1, y)

