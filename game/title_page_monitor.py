from game.data import DATA, GameState
from game.commands import Commands, CommandProcessor

class TitlePageMonitor:
    def __init__(self):
        pass

    def refresh(self):
        if DATA.state.run_state != GameState.RUN_STATE_STARTING:
            if not DATA.state.has_shown_title_page or DATA.state.show_title_page:
                CommandProcessor.queue_command(Commands.SHOW_TITLE_PAGE, [])
                DATA.state.has_shown_title_page = True
