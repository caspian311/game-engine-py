# pylint: disable=R0801
from cursed import CursedWindow

from game.commands.commands import Commands, CommandProcessor
from game.data import DATA, GameState
from game.title_page_helper import (title_page_content,
                                    calculate_title_prompt_position,
                                    calculate_title_position)
from game.player_helper import fighter_standing, calculate_player_position
from game.goblin_helper import goblins_content, calculate_goblin_position

class MainWindow(CursedWindow):
    X, Y = (0, 0)
    WIDTH, HEIGHT = (DATA.window["width"], DATA.window["height"] - 10)
    BORDERED = True


    goblins_content = []
    for g in range(3):
        with open(f"./artwork/goblins0{g+1}.txt", "r", encoding="UTF-8") as file:
            goblins_content.append([])
            for line in file:
                goblins_content[g].append(line)

    @classmethod
    def _middle_of_window_width(cls):
        return int(cls.WIDTH / 2)

    @classmethod
    def _middle_of_window_height(cls):
        return int(cls.HEIGHT / 2)

    @classmethod
    def update(cls):
        if DATA.state.run_state == GameState.QUITTING:
            cls.trigger('quit')

        cls._clear_screen(cls.WIDTH, cls.HEIGHT)

        if DATA.state.run_state == GameState.TITLE_PAGE:
            start_of_title_height = cls._handle_title_page()
            cls._handle_title_page_prompt(start_of_title_height)
        elif not DATA.user and DATA.state.run_state == GameState.USER_CREATION:
            if DATA.temp_user.name is None:
                DATA.temp_user.name = cls.getstr(5, 5, "What is your name? ")
            else:
                cls.addstr(
                        f"(A)ttack:      "
                        f"{cls._display_player_attribute(DATA.temp_user.attack)}", 5, 6)
                cls.addstr(
                        f"(D)efense:     "
                        f"{cls._display_player_attribute(DATA.temp_user.defense)}", 5, 7)
                cls.addstr(
                        f"(M)agic:       "
                        f"{cls._display_player_attribute(DATA.temp_user.magic)}", 5, 8)
                cls.addstr(
                        f"(C)onsitution: "
                        f"{cls._display_player_attribute(DATA.temp_user.constitution)}", 5, 9)
                cls.addstr("E(x)it", 5, 10)
                cls.addstr(
                        f"Points remaining: {DATA.temp_user.remaining_points}", 5, 12)

                k = cls.getch()
                if k == ord('a'):
                    DATA.temp_user.attack += 1
                    DATA.temp_user.remaining_points -= 1
                elif k == ord('d'):
                    DATA.temp_user.defense += 1
                    DATA.temp_user.remaining_points -= 1
                elif k == ord('m'):
                    DATA.temp_user.magic += 1
                    DATA.temp_user.remaining_points -= 1
                elif k == ord('c'):
                    DATA.temp_user.constitution += 1
                    DATA.temp_user.remaining_points -= 1
                elif k == ord('x'):
                    CommandProcessor.queue_command(Commands.CREATE_USER, [ DATA.temp_user.name,
                        DATA.temp_user.attack, DATA.temp_user.defense,
                        DATA.temp_user.magic, DATA.temp_user.constitution ])
        elif DATA.state.run_state == GameState.IN_BATTLE:
            cls._show_player()
            cls._show_npcs()

        if DATA.state.run_state == GameState.VICTORY:
            cls._display_status_message("VICTORY!")
        elif DATA.state.run_state == GameState.DEFEAT:
            cls._display_status_message("DEFEAT!")
        elif DATA.latest_message:
            cls._display_status_message(DATA.latest_message)

        cls.sleep(.1)
        cls.refresh()

    @classmethod
    def _display_player_attribute(cls, val):
        remaining = 10 - val
        beginning = "".join(["*" for x in range(val)])
        end = "".join(["-" for x in range(remaining)])
        return beginning + end

    @classmethod
    def _show_player(cls):
        start_player_width, start_player_height = calculate_player_position(
                cls._middle_of_window_width(),
                cls._middle_of_window_height())

        for index, line in enumerate(fighter_standing()):
            line = line.rstrip()
            cls.addstr(line, start_player_width, start_player_height + index)

    @classmethod
    def _show_npcs(cls):
        for idx, _ in enumerate(DATA.live_npcs()):
            start_goblin_width, start_goblin_height = calculate_goblin_position(
                    idx, len(DATA.live_npcs()),
                    cls._middle_of_window_width(), cls.HEIGHT)
            for index, line in enumerate(goblins_content[idx]):
                line = line.rstrip()
                cls.addstr(line, start_goblin_width, start_goblin_height + index)

    @classmethod
    def _display_status_message(cls, message):
        message_start_point = cls._middle_of_window_width() - int(len(message) / 2)
        cls.addstr(f"{message}", message_start_point, cls.HEIGHT - 3)

    @classmethod
    def _handle_title_page(cls):
        start_of_title, start_of_title_height = calculate_title_position(
                cls._middle_of_window_width(),
                cls._middle_of_window_height())

        for index, line in enumerate(title_page_content()):
            line = line.rstrip()
            cls.addstr(line, start_of_title, index + start_of_title_height)

        return start_of_title_height

    @classmethod
    def _handle_title_page_prompt(cls, start_of_title_height):
        title_prompt = "Press Any Key To Start"
        title_position, title_prompt_height = calculate_title_prompt_position(
                title_prompt, start_of_title_height, cls._middle_of_window_width())

        cls.addstr(f"{title_prompt}", title_position, title_prompt_height)
        k = cls.getch()
        if k is not None:
            CommandProcessor.queue_command(Commands.HIDE_TITLE_PAGE, [])

    @classmethod
    def _clear_screen(cls, width, height):
        line = "".join([" " for x in range(0, width-3)])
        for y in range(1, height-2):
            cls.addstr(line, 1, y)
