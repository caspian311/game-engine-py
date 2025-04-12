
class ConsoleManager():
    def __init__(self, game_engine):
        self._game_engine = game_engine

    def start_game(self):
        print("======Initial======")

        for player in self._game_engine.all_players():
            self.print_stats(player)

        print()

    def print_all_stats(self):
        for player in self._game_engine.all_players():
            self.print_stats(player)

    def print_stats(self, player):
        print(f"Name: {player.name()} ({player.strength()}) {self._health_progress_bar(player, 20)} ({player.current_health()}/{player.max_health()})")

    def _health_progress_bar(self, player, scale):
        percent_health_remaining = (player._current_health / player._max_health)
        health_scaled = int(percent_health_remaining * scale)

        lost_health_val = scale - health_scaled
        remaining_health_val = scale - lost_health_val

        lost_health = "-" * lost_health_val
        remaining_health = "#" * remaining_health_val
        percent_health = int(percent_health_remaining * 100)

        return f"{lost_health}{remaining_health}"


    def start_fight(self):
        print("======FIGHT!======")

    def start_round(self, x):
        print()
        print(f"===Round {x + 1}===")

    def invalid_option_alert(self):
        print("That's not a valid option!")

    def prompt_for_user_action(self):
        print("Options:")
        print("  Attack: a")
        print("  Defend: d")
        print("  Heal: h")

        action = input("What will you do? ")
        print(f"you chose {action}!")

        return action
