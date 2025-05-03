from game.monitors.battle import Battle
from game.data import DATA
from game.player_generator import PlayerGenerator

def test_battle_first_turn_is_user():
    DATA.user = PlayerGenerator.generate_user_player("John")
    DATA.clear_npcs()
    DATA.add_npc(PlayerGenerator.generate_goblin_player())
    DATA.add_npc(PlayerGenerator.generate_goblin_player())

    test_object = Battle()
    turn = test_object.next_turn()

    assert turn == DATA.user

def test_battle_second_turn_is_first_npc():
    goblin1 = PlayerGenerator.generate_goblin_player()

    DATA.user = PlayerGenerator.generate_user_player("John")
    DATA.clear_npcs()
    DATA.add_npc(goblin1)
    DATA.add_npc(PlayerGenerator.generate_goblin_player())

    test_object = Battle()
    test_object.next_turn()
    turn = test_object.next_turn()

    assert turn == goblin1

def test_battle_third_turn_is_second_npc():
    goblin2 = PlayerGenerator.generate_goblin_player()

    DATA.user = PlayerGenerator.generate_user_player("John")
    DATA.clear_npcs()
    DATA.add_npc(PlayerGenerator.generate_goblin_player())
    DATA.add_npc(goblin2)

    test_object = Battle()
    test_object.next_turn()
    test_object.next_turn()
    turn = test_object.next_turn()

    assert turn == goblin2

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

    assert turn == DATA.user
