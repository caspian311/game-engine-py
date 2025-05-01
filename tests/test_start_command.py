from game.start_command import StartCommand
from game.data import DATA, GameState

def test_execute_sets_run_state():
    DATA.state.run_state = -1

    StartCommand().execute([])

    assert GameState.STARTING == DATA.state.run_state
