from game_engine import GameEngine
from player import Player 
from player_generator import PlayerGenerator

def main():
    game_engine = GameEngine()
    player1 = PlayerGenerator.generate_player()
    player1.print_stats()

    player2 = PlayerGenerator.generate_player()
    player2.print_stats()

    game_engine.attack(player1, player2)

if __name__ == "__main__": main()
