import mock

from game.game import Game
from game.console_manager import ConsoleManager
from game.player_generator import PlayerGenerator
from game.player import Player
from game.user_player import UserPlayer
from game.npc_player import NpcPlayer

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

    assert game.is_over() is True

def test_player_lost_when_no_players():
    game = Game()

    assert game.player_lost() is True

def test_player_lost_when_alive_player():
    game = Game()

    with mock.patch.object(ConsoleManager, 'prompt_for_user_name'):
        game.add_player(PlayerGenerator.generate_user_player())

    assert game.player_lost() is False

def test_player_won_when_alive_player_and_no_npcs():
    game = Game()

    with mock.patch.object(ConsoleManager, 'prompt_for_user_name'):
        game.add_player(PlayerGenerator.generate_user_player())

    assert game.player_won() is True

def test_player_won_when_alive_player_and_living_npcs():
    game = Game()

    with mock.patch.object(ConsoleManager, 'prompt_for_user_name'):
        game.add_player(PlayerGenerator.generate_user_player())
    game.add_player(weak_player())
    game.add_player(strong_player())

    assert game.player_won() is False


def test_player_won_when_alive_player_and_all_npcs_dead():
    game = Game()

    with mock.patch.object(ConsoleManager, 'prompt_for_user_name'):
        game.add_player(PlayerGenerator.generate_user_player())
    game.add_player(blank_player())
    game.add_player(blank_player())

    assert game.player_won() is True


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

    assert game.user_player() is None

def test_user_player_when_just_npcs():
    game = Game()

    game.add_player(weak_player())
    game.add_player(weak_player())

    assert game.user_player() is None


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
def test_initially_game_is_not_over(_start_game, _player_won,
                                    _player_lost, _print_stats,
                                    _start_round, _prompt_for_user_action):
    game = Game()

    game.add_player(blank_player())
    game.add_player(weak_user())

    game.play()

    assert game.is_over() is True

def weak_player():
    p = Player('')
    p.override_max_health(1)
    p.override_current_health(1)
    p.override_attack(0)
    p.override_magic(0)
    p.override_defense(0)
    p.override_constitution(0)
    return p

def blank_player():
    p = Player('Blank')
    p.override_max_health(0)
    p.override_current_health(0)
    p.override_attack(0)
    p.override_magic(0)
    p.override_defense(0)
    p.override_constitution(0)
    return p

def weak_user():
    p = UserPlayer('Joe')
    p.override_max_health(1)
    p.override_current_health(1)
    p.override_attack(0)
    p.override_magic(0)
    p.override_defense(0)
    p.override_constitution(0)
    return p

def strong_player():
    p = NpcPlayer('John')
    p.override_max_health(100)
    p.override_current_health(100)
    p.override_attack(10)
    p.override_magic(10)
    p.override_defense(5)
    p.override_constitution(5)
    return p

def strong_user():
    p = UserPlayer('John')
    p.override_max_health(100)
    p.override_current_health(100)
    p.override_attack(10)
    p.override_magic(10)
    p.override_defense(5)
    p.override_constitution(5)
    return p
