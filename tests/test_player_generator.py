from game.player_generator import PlayerGenerator
from game.player import Player

def user():
    return PlayerGenerator.generate_user_player("Bob")

def npc():
    return PlayerGenerator.generate_npc_player()

def test_npc_player_has_random_name():
    assert len(npc().name()) > 0
    assert len(npc().name()) > 0
    assert len(npc().name()) > 0
    assert len(npc().name()) > 0
    assert len(npc().name()) > 0

def test_npc_player_are_not_users():
    assert not npc().is_user()

def test_user_player_are_users():
    assert user().is_user()

def test_npc_player_has_more_than_min_health():
    assert npc().max_health() >= Player.MIN_HEALTH
    assert npc().max_health() >= Player.MIN_HEALTH
    assert npc().max_health() >= Player.MIN_HEALTH
    assert npc().max_health() >= Player.MIN_HEALTH
    assert npc().max_health() >= Player.MIN_HEALTH

def test_npc_player_has_more_than_min_attack():
    assert npc().attack() >= Player.MIN_ATTACK
    assert npc().attack() >= Player.MIN_ATTACK
    assert npc().attack() >= Player.MIN_ATTACK
    assert npc().attack() >= Player.MIN_ATTACK
    assert npc().attack() >= Player.MIN_ATTACK

def test_npc_player_has_more_than_min_magic():
    assert npc().magic() >= Player.MIN_MAGIC
    assert npc().magic() >= Player.MIN_MAGIC
    assert npc().magic() >= Player.MIN_MAGIC
    assert npc().magic() >= Player.MIN_MAGIC
    assert npc().magic() >= Player.MIN_MAGIC

def test_npc_player_has_more_than_min_defense():
    assert npc().defense() >= Player.MIN_DEFENSE
    assert npc().defense() >= Player.MIN_DEFENSE
    assert npc().defense() >= Player.MIN_DEFENSE
    assert npc().defense() >= Player.MIN_DEFENSE
    assert npc().defense() >= Player.MIN_DEFENSE

def test_npc_player_has_more_than_min_constitution():
    assert npc().constitution() >= Player.MIN_CONSTITUTION
    assert npc().constitution() >= Player.MIN_CONSTITUTION
    assert npc().constitution() >= Player.MIN_CONSTITUTION
    assert npc().constitution() >= Player.MIN_CONSTITUTION
    assert npc().constitution() >= Player.MIN_CONSTITUTION

def test_user_player_has_more_than_min_health():
    assert user().max_health() >= Player.MIN_HEALTH
    assert user().max_health() >= Player.MIN_HEALTH
    assert user().max_health() >= Player.MIN_HEALTH
    assert user().max_health() >= Player.MIN_HEALTH
    assert user().max_health() >= Player.MIN_HEALTH

def test_user_player_has_more_than_min_attack():
    assert user().attack() >= Player.MIN_ATTACK
    assert user().attack() >= Player.MIN_ATTACK
    assert user().attack() >= Player.MIN_ATTACK
    assert user().attack() >= Player.MIN_ATTACK
    assert user().attack() >= Player.MIN_ATTACK

def test_user_player_has_more_than_min_magic():
    assert user().magic() >= Player.MIN_MAGIC
    assert user().magic() >= Player.MIN_MAGIC
    assert user().magic() >= Player.MIN_MAGIC
    assert user().magic() >= Player.MIN_MAGIC
    assert user().magic() >= Player.MIN_MAGIC

def test_user_player_has_more_than_min_defense():
    assert user().defense() >= Player.MIN_DEFENSE
    assert user().defense() >= Player.MIN_DEFENSE
    assert user().defense() >= Player.MIN_DEFENSE
    assert user().defense() >= Player.MIN_DEFENSE
    assert user().defense() >= Player.MIN_DEFENSE

def test_user_player_has_more_than_min_constitution():
    assert user().constitution() >= Player.MIN_CONSTITUTION
    assert user().constitution() >= Player.MIN_CONSTITUTION
    assert user().constitution() >= Player.MIN_CONSTITUTION
    assert user().constitution() >= Player.MIN_CONSTITUTION
    assert user().constitution() >= Player.MIN_CONSTITUTION
