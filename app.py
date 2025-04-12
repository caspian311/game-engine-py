from game_engine import GameEngine
from player import Player 
from player_generator import PlayerGenerator

def main():
    name = input("What's your name? ")

    game_engine = GameEngine()
    player1 = PlayerGenerator.generate_player(name)
    player2 = PlayerGenerator.generate_player()

    print("======Initial======")

    player1.print_stats()
    player2.print_stats()

    print()

    print("======FIGHT!======")

    for x in range(3):
        print(f"===Round {x + 1}===")

        print("Options:")
        print("  Attack: a")
        print("  Defend: d")
        print("  Heal: h")

        action = input("What will you do? ")
        print(f"you chose {action}!")
        match action:
            case "a":
                game_engine.attack(player1, player2)
            case "d":
                player1.defend()
            case "h":
                game_engine.heal(player1, 2)
            case _:
                print("That's not a valid option!")

        game_engine.attack(player2, player1)

        player1.print_stats()
        player2.print_stats()

        print()


if __name__ == "__main__": main()
