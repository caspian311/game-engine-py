from game.data import DATA, GameState
from game.commands.commands import Commands, CommandProcessor

class CreateUserMonitor:
    def __init__(self):
        pass

    def refresh(self):
        if DATA.user and DATA.state.run_state < GameState.IN_BATTLE:
            CommandProcessor.queue_command(Commands.START_BATTLE, [])
