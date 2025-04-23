from game import Game
from player_generator import PlayerGenerator

if __name__ == "__main__":
    game = Game()
    game.add_player(PlayerGenerator.generate_user_player())
    game.add_player(PlayerGenerator.generate_npc_player())

    game.play()
