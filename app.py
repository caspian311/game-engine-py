from game import Game
from game_engine import GameEngine
from player import Player 
from player_generator import PlayerGenerator
from console_manager import ConsoleManager

class App():
    def main(self):
        game = Game()
        game.add_player(PlayerGenerator.generate_user_player())
        game.add_player(PlayerGenerator.generate_npc_player())

        game.play()

if __name__ == "__main__": App().main()
