from game.data import DATA
from game.command import Command

class ShowTitlePageCommand(Command):
    def execute(self, _):
        DATA.state.show_title_page = True

class HideTitlePageCommand(Command):
    def execute(self, _):
        DATA.state.show_title_page = False
