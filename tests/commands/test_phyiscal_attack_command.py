from game.commands.physical_attack_command import PhysicalAttackCommand
from game.player import Player
from game.data import DATA

def test_attack_reduces_the_health_of_defender_by_difference_in_attack_and_def():
    attacker = Player('attacker')
    attacker.override_attack(10)
    defender = Player('defender')
    defender.override_current_health(100)
    defender.override_defense(2)

    assert 100 == defender.current_health()

    PhysicalAttackCommand().execute([attacker, defender])

    assert 92 == defender.current_health()

def test_attack_sets_a_latest_message():
    attacker = Player('attacker')
    attacker.override_attack(10)
    defender = Player('defender')
    defender.override_current_health(100)
    defender.override_defense(2)

    DATA.latest_message = None

    PhysicalAttackCommand().execute([attacker, defender])

    assert DATA.latest_message == "attacker attacked defender for 8 damage!"
