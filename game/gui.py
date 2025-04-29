from threading import Thread
from cursed import CursedApp, CursedWindow

from game.logger import log
from game.commands import Commands, CommandProcessor
from game.game_monitor import GameMonitor
from game.data import DATA, GameState

SCREEN_WIDTH, SCREEN_HEIGHT = (240, 55)

class TitleWindow(CursedWindow):
    X, Y = (0, 0)
    WIDTH, HEIGHT = (SCREEN_WIDTH, SCREEN_HEIGHT)
    BORDERED = True

    title_screen_content = []
    with open("./artwork/title-page.txt", "r", encoding="UTF-8") as file:
        for line in file:
            title_screen_content.append(line)

    @classmethod
    def update(cls):
        if DATA.state.run_state == GameState.RUN_STATE_QUITTING:
            cls.trigger('quit')

        if not DATA.state.show_title_page:
            return

        cls._clear_screen(cls.WIDTH, cls.HEIGHT)

        for line in TitleWindow.title_screen_content:
            cls.addstr(line, 5, 5)

        cls.addstr("Press Any Key To Start", 5, 20)
        cls.getch()

        cls.sleep(.1)
        cls.refresh()

    @classmethod
    def _clear_screen(cls, width, height):
        line = "".join([" " for x in range(0, width-3)])
        for y in range(1, height-2):
            cls.addstr(line, 1, y)

class MainWindow(CursedWindow):
    X, Y = (0, 0)
    WIDTH, HEIGHT = (SCREEN_WIDTH, SCREEN_HEIGHT - 10)
    BORDERED = True

    @classmethod
    def update(cls):
        if DATA.state.run_state == GameState.RUN_STATE_QUITTING:
            cls.trigger('quit')

        if DATA.state.show_title_page:
            return

        cls._clear_screen(cls.WIDTH, cls.HEIGHT)

        if DATA.state.prompt_for_user:
            name = cls.getstr(5, 5, "What is your name? ")
            CommandProcessor.queue_command(Commands.CREATE_USER, [name])
        elif DATA.state.show_victory:
            cls.addstr("VICTORY!", 5, 5)
        elif DATA.state.show_defeat:
            cls.addstr("DEFEAT!", 5, 5)

        cls.sleep(.1)
        cls.refresh()

    @classmethod
    def _clear_screen(cls, width, height):
        line = "".join([" " for x in range(0, width-3)])
        for y in range(1, height-2):
            cls.addstr(line, 1, y)


class UserActionsWindow(CursedWindow):
    X, Y = (0, SCREEN_HEIGHT - 10)
    WIDTH, HEIGHT = (int(SCREEN_WIDTH / 2) - 1, 10)
    BORDERED = True

    @classmethod
    def update(cls):
        if DATA.state.run_state == GameState.RUN_STATE_QUITTING:
            cls.trigger('quit')

        if DATA.state.show_title_page:
            return

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


class UserStatsWindow(CursedWindow):
    X, Y = (int(SCREEN_WIDTH / 2) + 1, SCREEN_HEIGHT - 10)
    WIDTH, HEIGHT = (int(SCREEN_WIDTH / 2) - 1, 10)
    BORDERED = True

    @classmethod
    def update(cls):
        if DATA.state.run_state == GameState.RUN_STATE_QUITTING:
            cls.trigger('quit')

        if DATA.state.show_title_page:
            return

        cls._clear_screen(cls.WIDTH, cls.HEIGHT)

        if DATA.state.in_battle:
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


def main():
    command_processor_thread = Thread(target=CommandProcessor.process)
    command_processor_thread.start()

    game_monitor_thread = Thread(target=GameMonitor.start_monitoring)
    game_monitor_thread.start()

    app = CursedApp()
    result = app.run()
    log(result)
    if result.interrupted():
        log('Ctrl-C pressed.')
    else:
        result.unwrap()

    command_processor_thread.join()
    game_monitor_thread.join()

    log("exiting")
