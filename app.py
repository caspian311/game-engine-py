from game_engine import GameEngine
from player import Player 
from player_generator import PlayerGenerator

def main():
    game_engine = GameEngine()
    player1 = PlayerGenerator.generate_player()
    player2 = PlayerGenerator.generate_player()

    print("===Initial===")

    player1.print_stats()
    player2.print_stats()

    print()

    for x in range(3):
        print(f"===Round {x + 1}===")

        game_engine.attack(player1, player2)

        player1.print_stats()
        player2.print_stats()

        print()


if __name__ == "__main__": main()
