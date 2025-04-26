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

@mock.patch.object(ConsoleManager, "magic_attack_results")
def test_magic_does_damage_of_magic_and_consitution_difference(_):
    attacker = Player("attacker 2")
    attacker.override_magic(10)
    defender = Player("defender 2")
    defender.override_max_health(100)
    defender.override_current_health(100)
    defender.override_constitution(3)

    GameEngine.magic_attack(attacker, defender)
    GameEngine.magic_attack(attacker, defender)

    assert 86 == defender.current_health()

@mock.patch.object(ConsoleManager, "magic_attack_results")
def test_magic_reports_to_console_manager(magic_attack_results):
    attacker = Player("attacker 2")
    attacker.override_magic(10)
    defender = Player("defender 2")
    defender.override_max_health(100)
    defender.override_current_health(100)
    defender.override_constitution(3)

    GameEngine.magic_attack(attacker, defender)

    magic_attack_results.assert_called_once_with("attacker 2", "defender 2", 7)

@mock.patch.object(ConsoleManager, "attack_results")
def test_attack_when_defending_results_in_half_damage(_):
    attacker = Player("attacker")
    attacker.override_attack(10)
    defender = Player("defender")
    defender.override_max_health(100)
    defender.override_current_health(100)
    defender.override_defense(2)

    defender.defend()

    GameEngine.attack(attacker, defender)

    assert 96 == defender.current_health()

@mock.patch.object(ConsoleManager, "attack_results")
def test_attack_when_defending_results_in_half_damage_only_once(_):
    attacker = Player("attacker")
    attacker.override_attack(10)
    defender = Player("defender")
    defender.override_max_health(100)
    defender.override_current_health(100)
    defender.override_defense(2)

    defender.defend()

    GameEngine.attack(attacker, defender)
    GameEngine.attack(attacker, defender)

    assert 88 == defender.current_health()
