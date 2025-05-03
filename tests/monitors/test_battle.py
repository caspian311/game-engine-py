from game.monitors.battle_monitor import Battle
from game.data import DATA
from game.player_generator import PlayerGenerator

def test_battle_first_turn_is_user():
    DATA.user = PlayerGenerator.generate_user_player("John")
    DATA.clear_npcs()
    DATA.add_npc(PlayerGenerator.generate_goblin_player())
    DATA.add_npc(PlayerGenerator.generate_goblin_player())

    test_object = Battle()
    turn = test_object.next_turn()

    assert turn.is_user()

def test_battle_second_turn_is_first_npc():
    DATA.user = PlayerGenerator.generate_user_player("John")
    DATA.clear_npcs()
    DATA.add_npc(PlayerGenerator.generate_goblin_player())
    DATA.add_npc(PlayerGenerator.generate_goblin_player())

    test_object = Battle()
    test_object.next_turn()
    turn = test_object.next_turn()

    assert not turn.is_user()

def test_battle_third_turn_is_second_npc():
    DATA.user = PlayerGenerator.generate_user_player("John")
    DATA.clear_npcs()
    DATA.add_npc(PlayerGenerator.generate_goblin_player())
    DATA.add_npc(PlayerGenerator.generate_goblin_player())

    test_object = Battle()
    test_object.next_turn()
    test_object.next_turn()
    turn = test_object.next_turn()

    assert not turn.is_user()

def test_battle_fourth_turn_is_back_to_user():
    DATA.user = PlayerGenerator.generate_user_player("John")
    DATA.clear_npcs()
    DATA.add_npc(PlayerGenerator.generate_goblin_player())
    DATA.add_npc(PlayerGenerator.generate_goblin_player())

    test_object = Battle()
    test_object.next_turn()
    test_object.next_turn()
    test_object.next_turn()
    turn = test_object.next_turn()

    assert turn.is_user()
