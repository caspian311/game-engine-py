import mock

from game_engine import GameEngine
from player import Player
from console_manager import ConsoleManager

@mock.patch.object(ConsoleManager, "attack_results")
def test_attack_does_damage_of_attack_and_defense_difference(_):
    attacker = Player("attacker")
    attacker.override_attack(5)
    defender = Player("defender")
    defender.override_max_health(100)
    defender.override_current_health(100)
    defender.override_defense(2)

    GameEngine.attack(attacker, defender)
    GameEngine.attack(attacker, defender)

    assert 94 == defender.current_health()

@mock.patch.object(ConsoleManager, "attack_results")
def test_attack_reports_to_console_manager(attack_results):
    attacker = Player("attacker 1")
    attacker.override_attack(5)
    defender = Player("defender 1")
    defender.override_max_health(100)
    defender.override_current_health(100)
    defender.override_defense(2)

    GameEngine.attack(attacker, defender)

    attack_results.assert_called_once_with("attacker 1", "defender 1", 3)
