from game.commands.defend_command import DefendCommand
from game.player import Player

def test_defend_commands_sets_player_to_defend():
    p = Player('test')

    assert not p.is_defending()

    DefendCommand().execute([p])

    assert p.is_defending()
