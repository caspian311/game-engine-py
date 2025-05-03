import mock

from game.data import DATA, GameState
from game.player import Player
from game.monitors.create_user_monitor import CreateUserMonitor
from game.commands.commands import CommandProcessor, Commands

@mock.patch.object(CommandProcessor, "queue_command")
def test_create_user_monitor_starts_a_battle_once_user_is_created(mock_queue_command):
    test_object = CreateUserMonitor()
    DATA.user = Player("dummy")
    DATA.state.run_state = GameState.STARTING

    test_object.refresh()

    mock_queue_command.assert_called_once_with(Commands.START_BATTLE, [])
