# pylint: disable=R0801
from cursed import CursedWindow

from game.commands.commands import Commands, CommandProcessor
from game.data import DATA, GameState
from game.logger import log

class MainWindow(CursedWindow):
    X, Y = (0, 0)
    WIDTH, HEIGHT = (DATA.window["width"], DATA.window["height"] - 10)
    BORDERED = True

    title_screen_content = []
    with open("./artwork/title-page.txt", "r", encoding="UTF-8") as file:
        for line in file:
            title_screen_content.append(line)

    fighter_standing_content = []
    with open("./artwork/fighter_standing.txt", "r", encoding="UTF-8") as file:
        for line in file:
            fighter_standing_content.append(line)

    goblins_content = []
    for g in range(3):
        with open(f"./artwork/goblins0{g+1}.txt", "r", encoding="UTF-8") as file:
            goblins_content.append([])
            for line in file:
                goblins_content[g].append(line)

    @classmethod
    def _middle_of_window_width(cls):
        return int(MainWindow.WIDTH / 2)

    @classmethod
    def _middle_of_window_height(cls):
        return int(MainWindow.HEIGHT / 2)

    @classmethod
    def update(cls):
        if DATA.state.run_state == GameState.QUITTING:
            cls.trigger('quit')

        cls._clear_screen(cls.WIDTH, cls.HEIGHT)

        if DATA.state.run_state == GameState.TITLE_PAGE:
            cls._handle_title_page()
        elif not DATA.user and DATA.state.run_state == GameState.USER_CREATION:
            name = cls.getstr(5, 5, "What is your name? ")
            CommandProcessor.queue_command(Commands.CREATE_USER, [name])
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
    def _show_player(cls):
        start_player_width, start_player_height = cls._calculate_player_position()

        for index, line in enumerate(MainWindow.fighter_standing_content):
            line = line.rstrip()
            cls.addstr(line, start_player_width, start_player_height + index)

    @classmethod
    def _calculate_player_position(cls):
        return (cls._calculate_player_width(), cls._calculate_player_height())

    @classmethod
    def _calculate_player_width(cls):
        player_width = len(MainWindow.fighter_standing_content[0])
        middle_of_player = int(player_width / 2)
        quarter_of_window = int(cls._middle_of_window_width() / 2)
        start_of_player = quarter_of_window - middle_of_player
        return start_of_player

    @classmethod
    def _calculate_player_height(cls):
        player_height = len(MainWindow.fighter_standing_content)
        middle_of_player = int(player_height / 2)
        middle_of_window = cls._middle_of_window_height()
        start_of_player = middle_of_window - middle_of_player
        return start_of_player

    @classmethod
    def _show_npcs(cls):
        for idx, _ in enumerate(DATA.live_npcs()):
            start_goblin_width, start_goblin_height = cls._calculate_goblin_position(
                    idx, len(DATA.live_npcs()))
            log(f"drawing goblins at {start_goblin_width}:{start_goblin_height}")
            for index, line in enumerate(MainWindow.goblins_content[idx]):
                line = line.rstrip()
                cls.addstr(line, start_goblin_width, start_goblin_height + index)


    @classmethod
    def _calculate_goblin_position(cls, g, max_goblins):
        return (cls._calculate_goblin_width(g), cls._calculate_goblin_height(g, max_goblins))

    @classmethod
    def _calculate_goblin_width(cls, g):
        goblin_width = len(MainWindow.goblins_content[g])
        middle_of_goblin = int(goblin_width / 2)
        quarter_of_window = int(cls._middle_of_window_width() / 2)
        start_of_goblin = (quarter_of_window * 3) - middle_of_goblin
        return start_of_goblin

    @classmethod
    def _calculate_goblin_height(cls, g, max_goblins):
        goblin_height = len(MainWindow.goblins_content[g])
        middle_of_goblin = int(goblin_height / 2)
        middle_of_window = int((cls.HEIGHT / (max_goblins + 1)) * (g + 1))
        start_of_goblin = middle_of_window - middle_of_goblin
        return start_of_goblin

    @classmethod
    def _display_status_message(cls, message):
        message_start_point = cls._middle_of_window_width() - int(len(message) / 2)
        cls.addstr(f"{message}", message_start_point, cls.HEIGHT - 3)

    @classmethod
    def _handle_title_page(cls):
        start_of_title, start_of_title_height = cls._calculate_title_position()

        for index, line in enumerate(MainWindow.title_screen_content):
            line = line.rstrip()
            cls.addstr(line, start_of_title, index + start_of_title_height)

        title_prompt = "Press Any Key To Start"
        title_position, title_prompt_height = cls._calculate_title_prompt_position(
                title_prompt, start_of_title_height)

        cls.addstr(f"{title_prompt}", title_position, title_prompt_height)
        k = cls.getch()
        if k is not None:
            CommandProcessor.queue_command(Commands.HIDE_TITLE_PAGE, [])

    @classmethod
    def _calculate_title_prompt_position(cls, title_prompt, start_of_title_height):
        middle_of_prompt = int(len(title_prompt) / 2)
        middle_of_window = cls._middle_of_window_width()
        title_position = middle_of_window - middle_of_prompt
        title_height = len(MainWindow.title_screen_content)

        title_prompt_height = start_of_title_height + title_height + 2
        return (title_position, title_prompt_height)

    @classmethod
    def _calculate_title_position(cls):
        return (cls._calculate_title_position_width(), cls._calculate_title_height())

    @classmethod
    def _calculate_title_position_width(cls):
        title_width = len(MainWindow.title_screen_content[0])
        middle_of_title = int(title_width / 2)
        middle_of_window = cls._middle_of_window_width()
        start_of_title = middle_of_window - middle_of_title
        return start_of_title

    @classmethod
    def _calculate_title_height(cls):
        title_height = len(MainWindow.title_screen_content)
        middle_of_title_height = int(title_height / 2)
        middle_of_window_height = cls._middle_of_window_height()
        start_of_title_height = middle_of_window_height - middle_of_title_height
        return start_of_title_height

    @classmethod
    def _clear_screen(cls, width, height):
        line = "".join([" " for x in range(0, width-3)])
        for y in range(1, height-2):
            cls.addstr(line, 1, y)
