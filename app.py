from game_engine import GameEngine
from player import Player 
from player_generator import PlayerGenerator
from console_manager import ConsoleManager

class App():
    def __init__(self):
        self._game_engine = GameEngine()
        self._console_manager = ConsoleManager(self._game_engine)

    def main(self):
        name = input("What's your name? ")

        user = PlayerGenerator.generate_player(name)
        player2 = PlayerGenerator.generate_player()

        self._game_engine.add_player(user)
        self._game_engine.add_npc(player2)

        self._console_manager.start_game()

        self._console_manager.start_fight()

        for x in range(3):
            self._console_manager.start_round(x)

            self._user_action(user, player2)

            self._npc_action(user)

            self._console_manager.print_all_stats()

    def _user_action(self, user, player2):
        action = self._console_manager.prompt_for_user_action()
        match action:
            case "a":
                self._game_engine.attack(user, player2)
            case "d":
                user.defend()
            case "h":
                self._game_engine.heal(user)
            case _:
                self._console_manager.invalid_option_alert()

    def _npc_action(self, user):
        for player in self._game_engine.all_npcs(): 
            self._game_engine.attack(player, user)

if __name__ == "__main__": App().main()
