from time import sleep

from game.data import DATA, GameState
from game.commands import Commands, CommandProcessor

class GameMonitor():
    @classmethod
    def start_monitoring(cls):
        while DATA.state.run_state != GameState.RUN_STATE_QUITTING:
            if DATA.state.run_state != GameState.RUN_STATE_STARTING:
                CommandProcessor.queue_command(Commands.START, [])
            elif not DATA.user:
                CommandProcessor.queue_command(Commands.PROMPT_FOR_USER, [])
            elif not DATA.state.in_battle:
                CommandProcessor.queue_command(Commands.START_BATTLE, [])
            elif len(DATA.live_npcs()) == 0:
                CommandProcessor.queue_command(Commands.UPDATE_GAME_STATE, [])

            sleep(1)
