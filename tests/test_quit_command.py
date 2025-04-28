from game.quit_command import QuitCommand
from game.data import DATA, GameState

def test_quit_command_sets_state_to_quitting():
    DATA.state.run_state = GameState.RUN_STATE_INIT

    QuitCommand().execute([])

    assert GameState.RUN_STATE_QUITTING == DATA.state.run_state
