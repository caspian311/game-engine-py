from game.data import DATA, GameState
from game.commands.command import Command
from game.logger import log

class StartCommand(Command):
    def execute(self, _):
        DATA.state.run_state = GameState.STARTING
        log(f"STARTCOMMAND: now current state is: {DATA.state.run_state}")
