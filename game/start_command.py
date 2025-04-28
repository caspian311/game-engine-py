from game.data import DATA, GameState
from game.command import Command

class StartCommand(Command):
    def execute(self, _):
        DATA.state.run_state = GameState.RUN_STATE_STARTING
