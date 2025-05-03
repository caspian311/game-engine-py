from game.data import DATA
from game.commands.command import Command

class WinBattleCommand(Command):
    def execute(self, arguments):
        DATA.state.in_battle = False
        DATA.state.show_victory = True
