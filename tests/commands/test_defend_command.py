from game.commands.defend_command import DefendCommand
from game.player import Player
from game.data import DATA

def test_defend_commands_sets_player_to_defend():
    p = Player('test')

    assert not p.is_defending()

    DefendCommand().execute([p])

    assert p.is_defending()

def test_defend_commands_sets_latest_message():
    p = Player('test')

    DefendCommand().execute([p])

    assert DATA.latest_message == "test defends!"
