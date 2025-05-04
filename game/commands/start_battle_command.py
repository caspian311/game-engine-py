import random

from game.commands.command import Command
from game.data import DATA, GameState
from game.player_generator import PlayerGenerator

class StartBattleCommand(Command):
    def execute(self, arguments):
        DATA.clear_npcs()

        for _ in range(self._how_many_baddies()):
            DATA.add_npc(PlayerGenerator.generate_goblin_player())

        DATA.state.run_state = GameState.IN_BATTLE

    def _how_many_baddies(self):
        return random.randint(1, 3)
