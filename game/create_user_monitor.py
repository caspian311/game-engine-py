from game.data import DATA
from game.commands import Commands, CommandProcessor

class CreateUserMonitor:
    def __init__(self):
        pass

    def refresh(self):
        if not DATA.state.has_shown_title_page or DATA.state.show_title_page:
            if not DATA.user:
                CommandProcessor.queue_command(Commands.PROMPT_FOR_USER, [])
