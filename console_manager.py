
class ConsoleManager():
    def start_game():
        print("======Initial======")
        print()

    def print_stats(player):
        print(f"Name: {player.name()} ({player.strength()}) {ConsoleManager._health_progress_bar(player, 20)} ({player.current_health()}/{player.max_health()})")

    def _health_progress_bar(player, scale):
        percent_health_remaining = (player._current_health / player._max_health)
        health_scaled = int(percent_health_remaining * scale)

        lost_health_val = scale - health_scaled
        remaining_health_val = scale - lost_health_val

        lost_health = "-" * lost_health_val
        remaining_health = "#" * remaining_health_val
        percent_health = int(percent_health_remaining * 100)

        return f"{lost_health}{remaining_health}"


    def start_fight():
        print("======FIGHT!======")

    def player_won():
        print("=============================")
        print("===========YOU WIN!==========")
        print("=============================")

    def player_lost():
        print("=============================")
        print("==========YOU LOST!==========")
        print("=============================")

    def start_round(x):
        print()
        print(f"===Round {x + 1}===")

    def invalid_option_alert():
        print("That's not a valid option!")

    def prompt_for_user_name():
        name = input("What's your name? ")
        return name

    def prompt_for_user_action():
        print("Options:")
        print("  Attack: a")
        print("  Defend: d")
        print("  Heal: h")

        action = input("What will you do? ")
        print(f"you chose {action}!")

        return action
