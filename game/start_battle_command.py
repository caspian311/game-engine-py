from game.command import Command
from game.data import DATA
from game.player_generator import PlayerGenerator

class StartBattleCommand(Command):
    def execute(self, arguments):
        DATA.add_npc(PlayerGenerator.generate_goblin_player())
        DATA.add_npc(PlayerGenerator.generate_goblin_player())

        DATA.state.in_battle = True
