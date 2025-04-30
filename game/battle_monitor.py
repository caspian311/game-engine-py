from game.data import DATA
from game.commands import Commands, CommandProcessor

class BattleMonitor:
    def __init__(self):
        pass

    def refresh(self):
        if DATA.state.has_shown_title_page and not DATA.state.show_title_page:
            if DATA.user:
                if not DATA.state.in_battle and not DATA.user.is_dead():
                    CommandProcessor.queue_command(Commands.START_BATTLE, [])
                elif len(DATA.live_npcs()) == 0:
                    CommandProcessor.queue_command(Commands.WIN_BATTLE, [])
                elif DATA.user.is_dead():
                    CommandProcessor.queue_command(Commands.LOSE_BATTLE, [])
                else:
                    baddie = DATA.live_npcs()[0]
                    user = DATA.user
                    CommandProcessor.queue_command(Commands.PHYSICAL_ATTACK, [baddie, user])
