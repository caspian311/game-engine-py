from threading import Thread
import mock

from game.monitors.game_monitor import GameMonitor
from game.commands.commands import Commands, CommandProcessor
from game.data import DATA, GameState

@mock.patch.object(CommandProcessor, "queue_command")
def test_game_monitor_sends_start(mock_queue_command):
    DATA.user = None
    DATA.state.run_state = GameState.INIT

    t = Thread(target=GameMonitor.start_monitoring)
    t.start()

    DATA.state.run_state = GameState.QUITTING
    t.join()

    mock_queue_command.assert_called_once_with(Commands.START, [])

@mock.patch.object(CommandProcessor, "queue_command")
def test_game_monitor_doesnt_start_if_already_started(mock_queue_command):
    DATA.user = None
    DATA.state.run_state = GameState.STARTING

    t = Thread(target=GameMonitor.start_monitoring)
    t.start()

    DATA.state.run_state = GameState.QUITTING
    t.join()

    assert mock_queue_command.called
    assert (Commands.START, []) != mock_queue_command.call_args[0]
