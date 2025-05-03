import mock

from game.monitors.battle import Battle
from game.data import DATA
from game.player_generator import PlayerGenerator
from game.commands.commands import CommandProcessor, Commands

def test_battle_if_player_has_no_move_take_turn_is_false():
    DATA.user = PlayerGenerator.generate_user_player("John")
    DATA.clear_npcs()
    DATA.add_npc(PlayerGenerator.generate_goblin_player())
    DATA.add_npc(PlayerGenerator.generate_goblin_player())

    test_object = Battle()

    assert test_object.take_turn() is False

@mock.patch.object(CommandProcessor, "queue_command")
def test_battle_if_player_has_no_move_dont_send_command(mock_queue_command):
    DATA.user = PlayerGenerator.generate_user_player("John")
    DATA.clear_npcs()
    DATA.add_npc(PlayerGenerator.generate_goblin_player())
    DATA.add_npc(PlayerGenerator.generate_goblin_player())

    test_object = Battle()

    test_object.take_turn()

    assert len(mock_queue_command.calls) == 0

def test_battle_if_player_has_move_take_turn_is_true():
    DATA.user = PlayerGenerator.generate_user_player("John")
    DATA.clear_npcs()
    DATA.add_npc(PlayerGenerator.generate_goblin_player())
    DATA.add_npc(PlayerGenerator.generate_goblin_player())

    test_object = Battle()

    DATA.user.set_turn("a")

    assert test_object.take_turn()

@mock.patch.object(CommandProcessor, "queue_command")
def test_battle_if_player_has_move_send_command(mock_queue_command):
    goblin1 = PlayerGenerator.generate_goblin_player()
    DATA.user = PlayerGenerator.generate_user_player("John")
    DATA.clear_npcs()
    DATA.add_npc(goblin1)
    DATA.add_npc(PlayerGenerator.generate_goblin_player())

    test_object = Battle()

    DATA.user.set_turn("a")
    test_object.take_turn()

    mock_queue_command.assert_called_once_with(Commands.PHYSICAL_ATTACK, [DATA.user, goblin1])

@mock.patch.object(CommandProcessor, "queue_command")
def test_battle_second_turn_is_first_npc(mock_queue_command):
    goblin1 = PlayerGenerator.generate_goblin_player()

    DATA.user = PlayerGenerator.generate_user_player("John")
    DATA.clear_npcs()
    DATA.add_npc(goblin1)
    DATA.add_npc(PlayerGenerator.generate_goblin_player())

    test_object = Battle()
    test_object.go_to_next_turn()

    test_object.take_turn()

    mock_queue_command.assert_called_once_with(Commands.PHYSICAL_ATTACK, [goblin1, DATA.user])

@mock.patch.object(CommandProcessor, "queue_command")
def test_battle_third_turn_is_second_npc(mock_queue_command):
    goblin2 = PlayerGenerator.generate_goblin_player()

    DATA.user = PlayerGenerator.generate_user_player("John")
    DATA.clear_npcs()
    DATA.add_npc(PlayerGenerator.generate_goblin_player())
    DATA.add_npc(goblin2)

    test_object = Battle()
    test_object.go_to_next_turn()
    test_object.go_to_next_turn()

    test_object.take_turn()

    mock_queue_command.assert_called_once_with(Commands.PHYSICAL_ATTACK, [goblin2, DATA.user])

@mock.patch.object(CommandProcessor, "queue_command")
def test_battle_fourth_turn_is_back_to_user(mock_queue_command):
    goblin2 = PlayerGenerator.generate_goblin_player()

    DATA.user = PlayerGenerator.generate_user_player("John")
    DATA.clear_npcs()
    DATA.add_npc(PlayerGenerator.generate_goblin_player())
    DATA.add_npc(goblin2)

    test_object = Battle()
    test_object.go_to_next_turn()
    test_object.go_to_next_turn()
    test_object.go_to_next_turn()

    test_object.take_turn()

    assert len(mock_queue_command.calls) == 0

@mock.patch.object(CommandProcessor, "queue_command")
def test_battle_fourth_turn_user_plays_if_has_a_turn(mock_queue_command):
    goblin1 = PlayerGenerator.generate_goblin_player()

    DATA.user = PlayerGenerator.generate_user_player("John")
    DATA.clear_npcs()
    DATA.add_npc(goblin1)
    DATA.add_npc(PlayerGenerator.generate_goblin_player())

    test_object = Battle()
    test_object.go_to_next_turn()
    test_object.go_to_next_turn()
    test_object.go_to_next_turn()

    DATA.user.set_turn("a")
    test_object.take_turn()

    mock_queue_command.assert_called_once_with(Commands.PHYSICAL_ATTACK, [DATA.user, goblin1])

@mock.patch.object(CommandProcessor, "queue_command")
def test_battle_user_attacks_next_available_npc(mock_queue_command):
    goblin1 = PlayerGenerator.generate_goblin_player()
    goblin2 = PlayerGenerator.generate_goblin_player()

    DATA.user = PlayerGenerator.generate_user_player("John")
    DATA.clear_npcs()
    DATA.add_npc(goblin1)
    DATA.add_npc(goblin2)

    test_object = Battle()

    DATA.user.set_turn("a")
    goblin1.override_current_health(0)
    test_object.take_turn()

    mock_queue_command.assert_called_once_with(Commands.PHYSICAL_ATTACK, [DATA.user, goblin2])

@mock.patch.object(CommandProcessor, "queue_command")
def test_battle_user_uses_magic_when_commanded(mock_queue_command):
    goblin1 = PlayerGenerator.generate_goblin_player()

    DATA.user = PlayerGenerator.generate_user_player("John")
    DATA.clear_npcs()
    DATA.add_npc(goblin1)

    test_object = Battle()

    DATA.user.set_turn("m")
    test_object.take_turn()

    mock_queue_command.assert_called_once_with(Commands.MAGIC_ATTACK, [DATA.user, goblin1])

@mock.patch.object(CommandProcessor, "queue_command")
def test_battle_user_uses_defends_when_commanded(mock_queue_command):
    goblin1 = PlayerGenerator.generate_goblin_player()

    DATA.user = PlayerGenerator.generate_user_player("John")
    DATA.clear_npcs()
    DATA.add_npc(goblin1)

    test_object = Battle()

    DATA.user.set_turn("d")
    test_object.take_turn()

    mock_queue_command.assert_called_once_with(Commands.DEFEND, [])

@mock.patch.object(CommandProcessor, "queue_command")
def test_battle_user_uses_heals_when_commanded(mock_queue_command):
    goblin1 = PlayerGenerator.generate_goblin_player()

    DATA.user = PlayerGenerator.generate_user_player("John")
    DATA.clear_npcs()
    DATA.add_npc(goblin1)

    test_object = Battle()

    DATA.user.set_turn("h")
    test_object.take_turn()

    mock_queue_command.assert_called_once_with(Commands.HEAL, [])

@mock.patch.object(CommandProcessor, "queue_command")
def test_battle_user_can_keep_taking_turns(mock_queue_command):
    DATA.user = PlayerGenerator.generate_user_player("John")
    DATA.clear_npcs()

    test_object = Battle()

    DATA.user.set_turn("h")
    assert test_object.take_turn()
    assert 1 == mock_queue_command.call_count

    DATA.user.set_turn("h")
    assert test_object.take_turn()
    assert 2 == mock_queue_command.call_count

def test_battle_user_no_longer_has_a_move_once_taken():
    DATA.user = PlayerGenerator.generate_user_player("John")
    DATA.clear_npcs()

    test_object = Battle()

    DATA.user.set_turn("h")
    assert test_object.take_turn()

    assert test_object.take_turn() is False
