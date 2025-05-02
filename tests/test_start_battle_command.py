from game.start_battle_command import StartBattleCommand
from game.data import DATA, GameState

def test_start_battle_command_adds_npcs():
    DATA.clear_npcs()
    assert 0 == len(DATA.live_npcs())

    StartBattleCommand().execute([])

    assert len(DATA.live_npcs()) > 0

def test_start_battle_command_sets_in_battle_state():
    DATA.state.in_battle = False

    StartBattleCommand().execute([])

    assert GameState.IN_BATTLE == DATA.state.run_state
