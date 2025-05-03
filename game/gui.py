from threading import Thread
from cursed import CursedApp

import game.main_window # pylint: disable=W0611
import game.user_action_window # pylint: disable=W0611
import game.user_stats_window # pylint: disable=W0611

from game.logger import log
from game.commands.commands import CommandProcessor
from game.monitors.game_monitor import GameMonitor

def main():
    command_processor_thread = Thread(target=CommandProcessor.process)
    command_processor_thread.start()

    game_monitor_thread = Thread(target=GameMonitor.start_monitoring)
    game_monitor_thread.start()

    app = CursedApp()
    result = app.run()
    log(result)
    if result.interrupted():
        log('Ctrl-C pressed.')
    else:
        result.unwrap()

    command_processor_thread.join()
    game_monitor_thread.join()

    log("exiting")
