from threading import Thread
import mock

from game.game_monitor import GameMonitor
from game.commands import Commands, CommandProcessor
from game.data import DATA, GameState
from game.player import Player

@mock.patch.object(CommandProcessor, "queue_command")
def test_game_monitor_sends_start(mock_queue_command):
    DATA.state.run_state = GameState.RUN_STATE_INIT

    t = Thread(target=GameMonitor.start_monitoring)
    t.start()

    DATA.state.run_state = GameState.RUN_STATE_QUITTING
    t.join()

    mock_queue_command.assert_called_once_with(Commands.START, [])

@mock.patch.object(CommandProcessor, "queue_command")
def test_game_monitor_doesnt_start_if_already_started(mock_queue_command):
    DATA.state.run_state = GameState.RUN_STATE_STARTING

    t = Thread(target=GameMonitor.start_monitoring)
    t.start()

    DATA.state.run_state = GameState.RUN_STATE_QUITTING
    t.join()

    assert mock_queue_command.called
    assert (Commands.START, []) != mock_queue_command.call_args[0]

@mock.patch.object(CommandProcessor, "queue_command")
def test_game_monitor_prompts_for_user_if_no_user_yet(mock_queue_command):
    DATA.state.run_state = GameState.RUN_STATE_STARTING
    DATA.user = None

    t = Thread(target=GameMonitor.start_monitoring)
    t.start()

    DATA.state.run_state = GameState.RUN_STATE_QUITTING
    t.join()

    mock_queue_command.assert_called_once_with(Commands.PROMPT_FOR_USER, [])

@mock.patch.object(CommandProcessor, "queue_command")
def test_game_monitor_doesnt_prompt_for_user_if_already_user(mock_queue_command):
    DATA.state.run_state = GameState.RUN_STATE_STARTING
    DATA.user = Player("")

    t = Thread(target=GameMonitor.start_monitoring)
    t.start()

    DATA.state.run_state = GameState.RUN_STATE_QUITTING
    t.join()

    assert mock_queue_command.called
    assert (Commands.PROMPT_FOR_USER, []) != mock_queue_command.call_args[0]
