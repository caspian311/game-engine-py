from game.data import DATA
from game.command import Command

class UpdateGameStateCommand(Command):
    def execute(self, arguments):
        DATA.state.in_battle = False
        DATA.state.show_victory = True
