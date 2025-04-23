import mock

from game import Game
from console_manager import ConsoleManager
from player_generator import PlayerGenerator
from player import Player
from user_player import UserPlayer
from npc_player import NpcPlayer

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
    game.add_player(weak_player())
    game.add_player(strong_player())

    assert game.player_won() == False


def test_player_won_when_alive_player_and_all_npcs_dead():
    game = Game()

    with mock.patch.object(ConsoleManager, 'prompt_for_user_name'):
        game.add_player(PlayerGenerator.generate_user_player())
    game.add_player(blank_player())
    game.add_player(blank_player())

    assert game.player_won() == True


def test_remaining_npcs_when_no_npcs():
    game = Game()

    assert len(game.remaining_npcs()) == 0


def test_remaining_npcs_when_one_live_npcs():
    game = Game()

    game.add_player(weak_player())

    assert len(game.remaining_npcs()) == 1

def test_remaining_npcs_when_multiple_npcs_some_dead():
    game = Game()

    game.add_player(weak_player())
    game.add_player(blank_player())
    game.add_player(weak_player())

    assert len(game.remaining_npcs()) == 2


def test_user_player_when_no_user():
    game = Game()

    assert game.user_player() == None

def test_user_player_when_just_npcs():
    game = Game()

    game.add_player(weak_player())
    game.add_player(weak_player())

    assert game.user_player() == None


def test_user_player_when_user_player():
    game = Game()

    game.add_player(weak_user())

    assert game.user_player().name() == "Joe"

def test_user_player_when_user_player_with_npcs():
    game = Game()

    game.add_player(weak_player())
    game.add_player(strong_user())
    game.add_player(weak_player())

    assert game.user_player().name() == "John"


def test_user_player_when_user_player_dead():
    game = Game()

    game.add_player(weak_player())
    game.add_player(weak_user())
    game.add_player(weak_player())

    assert game.user_player().name() == "Joe"


@mock.patch.object(ConsoleManager, 'start_game')
@mock.patch.object(ConsoleManager, 'player_won')
@mock.patch.object(ConsoleManager, 'player_lost')
@mock.patch.object(ConsoleManager, 'print_stats')
@mock.patch.object(ConsoleManager, 'start_round')
@mock.patch.object(ConsoleManager, 'prompt_for_user_action')
def test_initially_game_is_not_over(start_game, player_won, player_lost, print_stats, start_round, prompt_for_user_action):
    game = Game()

    game.add_player(blank_player())
    game.add_player(weak_user())

    game.play()

    assert game.is_over() == True

def weak_player():
    return Player('', 1, 0, 0, 0, 0)

def blank_player():
    return Player('', 0, 0, 0, 0, 0)

def weak_user():
    return UserPlayer('Joe', 1, 0, 0, 0, 0)

def strong_player():
    return NpcPlayer('John', 100, 100, 100, 5, 5)

def strong_user():
    return UserPlayer('John', 100, 100, 100, 5, 5)
