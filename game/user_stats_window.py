# pylint: disable=R0801
from cursed import CursedWindow

from game.commands import Commands, CommandProcessor
from game.data import DATA, GameState

class UserStatsWindow(CursedWindow):
    X, Y = (int(DATA.window["width"] / 2) + 1, DATA.window["height"] - 10)
    WIDTH, HEIGHT = (int(DATA.window["width"] / 2) - 1, 10)
    BORDERED = True

    @classmethod
    def update(cls):
        if DATA.state.run_state == GameState.QUITTING:
            cls.trigger('quit')

        cls._clear_screen(cls.WIDTH, cls.HEIGHT)

        if DATA.state.run_state == GameState.IN_BATTLE:
            cls._show_player_data(DATA.user, 0)

            for index, npc in enumerate(DATA.live_npcs()):
                cls._show_player_data(npc, (index * 2) + 3)

        k = cls.getch()
        if k == ord('q'):
            CommandProcessor.queue_command(Commands.QUIT, [])

        cls.sleep(.1)
        cls.refresh()

    @classmethod
    def _clear_screen(cls, width, height):
        line = "".join([" " for x in range(0, width-3)])
        for y in range(1, height-2):
            cls.addstr(line, 1, y)

    @classmethod
    def _show_player_data(cls, player, starting_line):
        player_info = f"Name: {player.name()} ({player.attack()}:{player.defense()})"
        health_bar = cls._health_progress_bar(player, 50)
        health_stats = f"{health_bar} {player.current_health()} / {player.max_health()}"

        cls.addstr(f"{player_info}", 1, starting_line)
        cls.addstr(f"{health_stats}", 1, starting_line + 1)

    @classmethod
    def _health_progress_bar(cls, player, scale):
        percent_health_remaining = (player.current_health() / player.max_health())
        health_scaled = int(percent_health_remaining * scale)

        lost_health_val = scale - health_scaled
        remaining_health_val = scale - lost_health_val

        lost_health = "-" * lost_health_val
        remaining_health = "#" * remaining_health_val

        return f"{lost_health}{remaining_health}"
