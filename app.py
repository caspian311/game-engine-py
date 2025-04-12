from game_engine import GameEngine
from player import Player 
from player_generator import PlayerGenerator
from console_manager import ConsoleManager

def main():
    name = input("What's your name? ")

    game_engine = GameEngine()
    console_manager = ConsoleManager(game_engine)
    player1 = PlayerGenerator.generate_player(name)
    player2 = PlayerGenerator.generate_player()
    game_engine.add_player(player1)
    game_engine.add_player(player2)

    console_manager.start_game()

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

        console_manager.print_stats(player1)
        console_manager.print_stats(player2)

        print()


if __name__ == "__main__": main()
