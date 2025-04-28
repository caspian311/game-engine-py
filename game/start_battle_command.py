from game.command import Command
from game.data import DATA
from game.npc_player import NpcPlayer

class StartBattleCommand(Command):
    def execute(self, arguments):
        DATA.add_npc(NpcPlayer('Goblin 1'))
        DATA.add_npc(NpcPlayer('Goblin 2'))

        DATA.state.in_battle = True
