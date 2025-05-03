from game.commands.heal_command import HealCommand
from game.game_engine import GameEngine
from game.player import Player
from game.data import DATA

def test_heal_command_increases_players_health():
    p = Player('healer')
    current_health = p.current_health()

    HealCommand().execute([p])

    assert current_health + GameEngine.HEAL_AMOUNT == p.current_health()

def test_heal_sets_a_latest_message():
    p = Player('healer')

    DATA.latest_message = None

    HealCommand().execute([p])

    assert DATA.latest_message == "healer heals by 2!"
