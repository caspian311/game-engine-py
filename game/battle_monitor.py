from game.data import DATA, GameState
from game.commands import Commands, CommandProcessor

class BattleMonitor:
    def __init__(self):
        pass

    def refresh(self):
        if DATA.state.run_state == GameState.IN_BATTLE:
            if len(DATA.live_npcs()) > 0:
                baddie = DATA.live_npcs()[0]
                user = DATA.user
                CommandProcessor.queue_command(Commands.PHYSICAL_ATTACK, [baddie, user])

        if DATA.state.run_state == GameState.IN_BATTLE and len(DATA.live_npcs()) == 0:
            DATA.state.run_state = GameState.VICTORY

        if DATA.state.run_state == GameState.IN_BATTLE and DATA.user.is_dead():
            DATA.state.run_state = GameState.DEFEAT
