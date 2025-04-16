import mock

from game import Game
from console_manager import ConsoleManager
from player_generator import PlayerGenerator

def test_all_players_with_no_players():
    game = Game()

    assert len(game.all_players()) == 0

def test_all_players_with_one_players():
    game = Game()
    game.add_player(PlayerGenerator.generate_npc_player())

    assert len(game.all_players()) == 1

def test_all_players_with_a_mix_of_players():
    game = Game()

    with mock.patch.object(ConsoleManager, 'prompt_for_user_name'):
        game.add_player(PlayerGenerator.generate_npc_player())
        game.add_player(PlayerGenerator.generate_user_player())
        game.add_player(PlayerGenerator.generate_npc_player())

        assert len(game.all_players()) == 3

def test_is_over_when_no_players():
    game = Game()

    assert game.is_over() == True

def test_player_lost_when_no_players():
    game = Game()

    assert game.player_lost() == True

def test_player_lost_when_alive_player():
    game = Game()

    with mock.patch.object(ConsoleManager, 'prompt_for_user_name'):
        game.add_player(PlayerGenerator.generate_user_player())

    assert game.player_lost() == False

def test_player_won_when_alive_player_and_no_npcs():
    game = Game()

    with mock.patch.object(ConsoleManager, 'prompt_for_user_name'):
        game.add_player(PlayerGenerator.generate_user_player())

    assert game.player_won() == True

def test_player_won_when_alive_player_and_living_npcs():
    game = Game()

    with mock.patch.object(ConsoleManager, 'prompt_for_user_name'):
        game.add_player(PlayerGenerator.generate_user_player())
        game.add_player(PlayerGenerator.generate_npc_player())

    assert game.player_won() == False





