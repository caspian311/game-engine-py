import mock

from game import Game
from console_manager import ConsoleManager
from player_generator import PlayerGenerator
from player import Player
from user_player import UserPlayer

def user():
    return PlayerGenerator.generate_user_player()

def npc():
    return PlayerGenerator.generate_npc_player()

def test_npc_player_has_more_than_min_health():
    assert npc().max_health() >= PlayerGenerator.MIN_HEALTH
    assert npc().max_health() >= PlayerGenerator.MIN_HEALTH
    assert npc().max_health() >= PlayerGenerator.MIN_HEALTH
    assert npc().max_health() >= PlayerGenerator.MIN_HEALTH
    assert npc().max_health() >= PlayerGenerator.MIN_HEALTH

def test_npc_player_has_more_than_min_attack():
    assert npc().attack() >= PlayerGenerator.MIN_ATTACK
    assert npc().attack() >= PlayerGenerator.MIN_ATTACK
    assert npc().attack() >= PlayerGenerator.MIN_ATTACK
    assert npc().attack() >= PlayerGenerator.MIN_ATTACK
    assert npc().attack() >= PlayerGenerator.MIN_ATTACK

@mock.patch.object(ConsoleManager, 'prompt_for_user_name', return_value="test")
def test_user_player_has_more_than_min_health(_):
    assert user().max_health() >= PlayerGenerator.MIN_HEALTH
    assert user().max_health() >= PlayerGenerator.MIN_HEALTH
    assert user().max_health() >= PlayerGenerator.MIN_HEALTH
    assert user().max_health() >= PlayerGenerator.MIN_HEALTH
    assert user().max_health() >= PlayerGenerator.MIN_HEALTH

@mock.patch.object(ConsoleManager, 'prompt_for_user_name', return_value="test")
def test_user_player_has_more_than_min_attack(_):
    assert user().attack() >= PlayerGenerator.MIN_ATTACK
    assert user().attack() >= PlayerGenerator.MIN_ATTACK
    assert user().attack() >= PlayerGenerator.MIN_ATTACK
    assert user().attack() >= PlayerGenerator.MIN_ATTACK
    assert user().attack() >= PlayerGenerator.MIN_ATTACK
