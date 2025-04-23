import mock

from console_manager import ConsoleManager
from player_generator import PlayerGenerator

def user():
    return PlayerGenerator.generate_user_player()

def npc():
    return PlayerGenerator.generate_npc_player()

def test_npc_player_has_random_name():
    assert len(npc().name()) > 0
    assert len(npc().name()) > 0
    assert len(npc().name()) > 0
    assert len(npc().name()) > 0
    assert len(npc().name()) > 0

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

def test_npc_player_has_more_than_min_magic():
    assert npc().magic() >= PlayerGenerator.MIN_MAGIC
    assert npc().magic() >= PlayerGenerator.MIN_MAGIC
    assert npc().magic() >= PlayerGenerator.MIN_MAGIC
    assert npc().magic() >= PlayerGenerator.MIN_MAGIC
    assert npc().magic() >= PlayerGenerator.MIN_MAGIC

def test_npc_player_has_more_than_min_defense():
    assert npc().defense() >= PlayerGenerator.MIN_DEFENSE
    assert npc().defense() >= PlayerGenerator.MIN_DEFENSE
    assert npc().defense() >= PlayerGenerator.MIN_DEFENSE
    assert npc().defense() >= PlayerGenerator.MIN_DEFENSE
    assert npc().defense() >= PlayerGenerator.MIN_DEFENSE

def test_npc_player_has_more_than_min_constitution():
    assert npc().constitution() >= PlayerGenerator.MIN_CONSTITUTION
    assert npc().constitution() >= PlayerGenerator.MIN_CONSTITUTION
    assert npc().constitution() >= PlayerGenerator.MIN_CONSTITUTION
    assert npc().constitution() >= PlayerGenerator.MIN_CONSTITUTION
    assert npc().constitution() >= PlayerGenerator.MIN_CONSTITUTION

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

@mock.patch.object(ConsoleManager, 'prompt_for_user_name', return_value="test")
def test_user_player_has_more_than_min_magic(_):
    assert user().magic() >= PlayerGenerator.MIN_MAGIC
    assert user().magic() >= PlayerGenerator.MIN_MAGIC
    assert user().magic() >= PlayerGenerator.MIN_MAGIC
    assert user().magic() >= PlayerGenerator.MIN_MAGIC
    assert user().magic() >= PlayerGenerator.MIN_MAGIC

@mock.patch.object(ConsoleManager, 'prompt_for_user_name', return_value="test")
def test_user_player_has_more_than_min_defense(_):
    assert user().defense() >= PlayerGenerator.MIN_DEFENSE
    assert user().defense() >= PlayerGenerator.MIN_DEFENSE
    assert user().defense() >= PlayerGenerator.MIN_DEFENSE
    assert user().defense() >= PlayerGenerator.MIN_DEFENSE
    assert user().defense() >= PlayerGenerator.MIN_DEFENSE

@mock.patch.object(ConsoleManager, 'prompt_for_user_name', return_value="test")
def test_user_player_has_more_than_min_constitution(_):
    assert user().constitution() >= PlayerGenerator.MIN_CONSTITUTION
    assert user().constitution() >= PlayerGenerator.MIN_CONSTITUTION
    assert user().constitution() >= PlayerGenerator.MIN_CONSTITUTION
    assert user().constitution() >= PlayerGenerator.MIN_CONSTITUTION
    assert user().constitution() >= PlayerGenerator.MIN_CONSTITUTION

