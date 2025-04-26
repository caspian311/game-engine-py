from game.game import Game
from game.player_generator import PlayerGenerator

def app():
    game = Game()
    game.add_player(PlayerGenerator.generate_user_player())
    game.add_player(PlayerGenerator.generate_npc_player())

    game.play()
