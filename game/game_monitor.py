from time import sleep

from game.data import DATA, GameState
from game.commands import Commands, CommandProcessor
from game.game_state_monitor import GameStateMonitor
from game.title_page_monitor import TitlePageMonitor
from game.create_user_monitor import CreateUserMonitor
from game.battle_monitor import BattleMonitor

class GameMonitor():
    game_state_monitor = GameStateMonitor()
    title_page_monitor = TitlePageMonitor()
    create_user_monitor = CreateUserMonitor()
    battle_monitor = BattleMonitor()

    @classmethod
    def start_monitoring(cls):
        while DATA.state.run_state != GameState.RUN_STATE_QUITTING:
            cls.game_state_monitor.refresh()
            cls.title_page_monitor.refresh()
            cls.create_user_monitor.refresh()
            cls.battle_monitor.refresh()

            sleep(1)
