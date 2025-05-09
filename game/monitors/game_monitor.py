from time import sleep

from game.data import DATA, GameState
from game.monitors.game_state_monitor import GameStateMonitor
from game.monitors.title_page_monitor import TitlePageMonitor
from game.monitors.create_user_monitor import CreateUserMonitor
from game.monitors.battle_monitor import BattleMonitor
from game.logger import log

class GameMonitor():
    game_state_monitor = GameStateMonitor()
    title_page_monitor = TitlePageMonitor()
    create_user_monitor = CreateUserMonitor()
    battle_monitor = BattleMonitor()

    @classmethod
    def start_monitoring(cls):
        while DATA.state.run_state != GameState.QUITTING:
            try:
                cls.game_state_monitor.refresh()
                cls.title_page_monitor.refresh()
                cls.create_user_monitor.refresh()
                cls.battle_monitor.refresh()
            except Exception as e: # pylint: disable=broad-exception-caught
                log(f"GAMEMONITOR: {e}")

            sleep(1)
