import mock

from game.data import DATA, GameState
from game.title_page_monitor import TitlePageMonitor
from game.commands.commands import CommandProcessor, Commands

@mock.patch.object(CommandProcessor, "queue_command")
def test_title_page_monitor_shows_title_page_when_starting(mock_queue_command):
    test_object = TitlePageMonitor()
    DATA.state.run_state = GameState.STARTING

    test_object.refresh()

    mock_queue_command.assert_called_once_with(Commands.SHOW_TITLE_PAGE, [])
