# pylint: disable=R0801
from cursed import CursedWindow

from game.commands.commands import Commands, CommandProcessor
from game.data import DATA, GameState

class MainWindow(CursedWindow):
    X, Y = (0, 0)
    WIDTH, HEIGHT = (DATA.window["width"], DATA.window["height"] - 10)
    BORDERED = True

    title_screen_content = []
    with open("./artwork/title-page.txt", "r", encoding="UTF-8") as file:
        for line in file:
            title_screen_content.append(line)

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
        elif DATA.state.run_state == GameState.VICTORY:
            cls.addstr("VICTORY!", 5, 5)
        elif DATA.state.run_state == GameState.DEFEAT:
            cls.addstr("DEFEAT!", 5, 5)

        cls.sleep(.1)
        cls.refresh()

    @classmethod
    def _handle_title_page(cls):
        start_of_title, start_of_title_height = cls._calculate_title_position()

        for index, line in enumerate(MainWindow.title_screen_content):
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
        middle_of_window = int(MainWindow.WIDTH / 2)
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
        middle_of_window = int(MainWindow.WIDTH / 2)
        start_of_title = middle_of_window - middle_of_title
        return start_of_title

    @classmethod
    def _calculate_title_height(cls):
        title_height = len(MainWindow.title_screen_content)
        middle_of_title_height = int(title_height / 2)
        middle_of_window_height = int(MainWindow.HEIGHT / 2)
        start_of_title_height = middle_of_window_height - middle_of_title_height
        return start_of_title_height

    @classmethod
    def _clear_screen(cls, width, height):
        line = "".join([" " for x in range(0, width-3)])
        for y in range(1, height-2):
            cls.addstr(line, 1, y)
