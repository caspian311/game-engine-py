from game.win_battle_command import WinBattleCommand
from game.data import DATA

def test_win_battle_command_sets_in_battle_state():
    DATA.state.in_battle = True

    WinBattleCommand().execute([])

    assert not DATA.state.in_battle

def test_win_battle_command_sets_show_victory_state():
    DATA.state.show_victory = False

    WinBattleCommand().execute([])

    assert DATA.state.show_victory
