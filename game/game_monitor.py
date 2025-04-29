from time import sleep

from game.data import DATA, GameState
from game.commands import Commands, CommandProcessor

class GameMonitor():
    @classmethod
    def start_monitoring(cls):
        while DATA.state.run_state != GameState.RUN_STATE_QUITTING:
            if DATA.state.run_state != GameState.RUN_STATE_STARTING:
                CommandProcessor.queue_command(Commands.START, [])
                # TODO show title page
            elif not DATA.user:
                CommandProcessor.queue_command(Commands.PROMPT_FOR_USER, [])
            elif not DATA.state.in_battle and not DATA.user.is_dead():
                CommandProcessor.queue_command(Commands.START_BATTLE, [])
            elif len(DATA.live_npcs()) == 0:
                CommandProcessor.queue_command(Commands.WIN_BATTLE, [])
            elif DATA.user.is_dead():
                CommandProcessor.queue_command(Commands.LOSE_BATTLE, [])
            else:
                baddie = DATA.live_npcs()[0]
                user = DATA.user
                CommandProcessor.queue_command(Commands.PHYSICAL_ATTACK, [baddie, user])

            sleep(1)
