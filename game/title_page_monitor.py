from game.data import DATA, GameState
from game.commands import Commands, CommandProcessor

class TitlePageMonitor:
    def __init__(self):
        pass

    def refresh(self):
        if DATA.state.run_state == GameState.STARTING:
            CommandProcessor.queue_command(Commands.SHOW_TITLE_PAGE, [])
