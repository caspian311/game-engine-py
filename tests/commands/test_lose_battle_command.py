from game.commands.lose_battle_command import LoseBattleCommand
from game.data import DATA

def test_lose_battle_command_sets_in_battle_to_false():
    DATA.state.in_battle = True

    LoseBattleCommand().execute([])

    assert not DATA.state.in_battle

def test_lose_battle_command_sets_show_defeat_to_true():
    DATA.state.show_defeat = False

    LoseBattleCommand().execute([])

    assert DATA.state.show_defeat
