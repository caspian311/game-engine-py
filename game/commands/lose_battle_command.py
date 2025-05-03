from game.data import DATA
from game.commands.command import Command

class LoseBattleCommand(Command):
    def execute(self, arguments):
        DATA.state.in_battle = False
        DATA.state.show_defeat = True
