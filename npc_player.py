from game_engine import GameEngine
from player import Player

class NpcPlayer(Player):
    def take_turn(self, game):
        GameEngine.attack(self, game.user_player())
