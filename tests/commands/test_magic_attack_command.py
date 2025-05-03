from game.commands.magic_attack_command import MagicAttackCommand
from game.player import Player
from game.data import DATA

def test_magic_attack_reduces_the_health_of_defender_by_difference_in_magic_and_const():
    attacker = Player('attacker')
    attacker.override_magic(10)
    defender = Player('defender')
    defender.override_current_health(100)
    defender.override_constitution(2)

    assert 100 == defender.current_health()

    MagicAttackCommand().execute([attacker, defender])

    assert 92 == defender.current_health()

def test_magic_attack_sets_a_latest_message():
    attacker = Player('attacker')
    attacker.override_magic(10)
    defender = Player('defender')
    defender.override_current_health(100)
    defender.override_constitution(2)

    DATA.latest_message = None

    MagicAttackCommand().execute([attacker, defender])

    assert DATA.latest_message == "attacker attacked defender with MAGIC for 8 damage!"
