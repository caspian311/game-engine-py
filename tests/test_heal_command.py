from game.heal_command import HealCommand
from game.game_engine import GameEngine
from game.player import Player

def test_heal_command_increases_players_health():
    p = Player('healer')
    current_health = p.current_health()

    HealCommand().execute([p])

    assert current_health + GameEngine.HEAL_AMOUNT == p.current_health()
