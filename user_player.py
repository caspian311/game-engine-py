from game_engine import GameEngine
from console_manager import ConsoleManager
from player import Player

class UserPlayer(Player):
    def take_turn(self, game):
        target = self._first_npc(game)

        action = ConsoleManager.prompt_for_user_action()
        match action:
            case "a":
                GameEngine.attack(self, target)
            case "m":
                GameEngine.magic_attack(self, target)
            case "d":
                self.defend()
            case "h":
                GameEngine.heal(self)
            case _:
                ConsoleManager.invalid_option_alert()

    def is_user(self):
        return True

    def _first_npc(self, game):
        return [p for p in game.all_players() if not p.is_user()][0]
