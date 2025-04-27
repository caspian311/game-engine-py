from threading import Thread
from time import sleep
from cursed import CursedApp, CursedWindow, CursedMenu

from game.logger import log
from game.command_processor import CommandProcessor
from game.commands import Commands
from game.data import DATA


SCREEN_WIDTH, SCREEN_HEIGHT = (240, 55)

class MainWindow(CursedWindow):
    X, Y = (0, 0)
    WIDTH, HEIGHT = (SCREEN_WIDTH, SCREEN_HEIGHT - 10)
    BORDERED = True

    @classmethod
    def update(cls):
        if not DATA.state.running:
            cls.trigger('quit')

        cls.addstr(f"Prompt for user? {DATA.state.prompt_for_user}", 2, 1)
        cls.addstr(f"User? {DATA.user.name() if DATA.user else "none"}", 2, 2)
        cls.addstr(f"NPCs? {len(DATA.npcs)}", 2, 3)

        if DATA.state.prompt_for_user:
            name = cls.getstr(5, 5, "What is your name? ")
            CommandProcessor.queue_command(Commands.CREATE_USER, [name])
        else:
            line = "".join([" " for x in range(0, cls.WIDTH-3)])
            for y in range(1, cls.HEIGHT-2):
                cls.addstr(line, 1, y)
                    
        cls.addstr(f"Prompt for user? {DATA.state.prompt_for_user}", 2, 1)
        cls.addstr(f"User? {DATA.user.name() if DATA.user else "none"}", 2, 2)
        cls.addstr(f"NPCs? {len(DATA.npcs)}", 2, 3)

        cls.sleep(.1)
        cls.refresh()

class UserActionsWindow(CursedWindow):
    X, Y = (0, SCREEN_HEIGHT - 10)
    WIDTH, HEIGHT = (int(SCREEN_WIDTH / 2) - 1, 10)
    BORDERED = True

    @classmethod
    def update(cls):
        if not DATA.state.running:
            cls.trigger('quit')

        if not DATA.state.prompt_for_user:
            cls.addstr("Choose your action:", 1, 2)
            cls.addstr("A: ATTACK", 1, 3)
            cls.addstr("M: MAGIC", 1, 4)
            cls.addstr("D: DEFEND", 1, 5)
            cls.addstr("H: HEAL", 1, 6)

        k = cls.getch()
        if k == ord('a'):
            CommandProcessor.queue_command(Commands.PHYSICAL_ATTACK, [DATA.user, DATA.npcs[0]])
        elif k == ord('m'):
            CommandProcessor.queue_command(Commands.MAGIC_ATTACK, [DATA.user, DATA.npcs[0]])
        elif k == ord('d'):
            CommandProcessor.queue_command(Commands.DEFEND, [DATA.user])
        elif k == ord('h'):
            CommandProcessor.queue_command(Commands.HEAL, [DATA.user])

        cls.sleep(.1)
        cls.refresh()

class UserStatsWindow(CursedWindow):
    X, Y = (int(SCREEN_WIDTH / 2) + 1, SCREEN_HEIGHT - 10)
    WIDTH, HEIGHT = (int(SCREEN_WIDTH / 2) - 1, 10)
    BORDERED = True

    @classmethod
    def update(cls):
        if not DATA.state.running:
            cls.trigger('quit')

        if not DATA.state.prompt_for_user:
            cls._show_player_data(DATA.user, 0)
            for index, npc in enumerate(DATA.npcs):
                cls._show_player_data(npc, (index * 2) + 3)

        k = cls.getch()
        if k == ord('q'):
            CommandProcessor.queue_command(Commands.QUIT, [])

        cls.sleep(.1)
        cls.refresh()

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
    thread = Thread(target=CommandProcessor.process)
    thread.start()

    CommandProcessor.queue_command(Commands.START, [])

    app = CursedApp()
    result = app.run()
    log(result)
    if result.interrupted():
        log('Ctrl-C pressed.')
    else:
        result.unwrap()
    thread.join()
    log("exiting")
