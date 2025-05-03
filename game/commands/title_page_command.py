from game.data import DATA, GameState
from game.commands.command import Command

class ShowTitlePageCommand(Command):
    def execute(self, _):
        DATA.state.run_state = GameState.TITLE_PAGE

class HideTitlePageCommand(Command):
    def execute(self, _):
        DATA.state.run_state = GameState.USER_CREATION
