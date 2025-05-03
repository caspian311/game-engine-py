from game.commands.command import Command
from game.data import DATA, GameState

class QuitCommand(Command):
    def execute(self, arguments):
        DATA.state.run_state = GameState.QUITTING

        DATA.latest_message = "Goodbye!"
