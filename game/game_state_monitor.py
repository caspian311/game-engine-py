from game.data import DATA, GameState
from game.commands import Commands, CommandProcessor

class GameStateMonitor:
    def __init__(self):
        pass

    def refresh(self):
        if DATA.state.run_state != GameState.RUN_STATE_STARTING:
            CommandProcessor.queue_command(Commands.START, [])
