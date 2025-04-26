class ConsoleManager():
    @classmethod
    def attack_results(cls, attacker, defender, damage_delt):
        print((
            f"{attacker} attacks {defender} "
            f"and does {damage_delt} damage!"
            ))
        print()

    @classmethod
    def magic_attack_results(cls, attacker, defender, damage_delt):
        print((
            f"{attacker} attacks {defender} "
            f"with MAGIC and does {damage_delt} damage!"
            ))

    @classmethod
    def heal_results(cls, player_name, amount):
        print(f"{player_name} heals for {amount} health!")

    @classmethod
    def start_game(cls):
        print("======Initial======")
        print()

    @classmethod
    def print_stats(cls, player):
        print((
            f"Name: {player.name()} ({player.attack()}:{player.defense()}) "
            f"{cls._health_progress_bar(player, 20)} "
            f"({player.current_health()}/{player.max_health()})"
            ))

    @classmethod
    def _health_progress_bar(cls, player, scale):
        percent_health_remaining = (player.current_health() / player.max_health())
        health_scaled = int(percent_health_remaining * scale)

        lost_health_val = scale - health_scaled
        remaining_health_val = scale - lost_health_val

        lost_health = "-" * lost_health_val
        remaining_health = "#" * remaining_health_val

        return f"{lost_health}{remaining_health}"

    @classmethod
    def start_fight(cls):
        print("======FIGHT!======")

    @classmethod
    def player_won(cls):
        print("=============================")
        print("===========YOU WIN!==========")
        print("=============================")

    @classmethod
    def player_lost(cls):
        print("=============================")
        print("==========YOU LOST!==========")
        print("=============================")

    @classmethod
    def start_round(cls, x):
        print()
        print(f"===Round {x + 1}===")

    @classmethod
    def invalid_option_alert(cls):
        print("That's not a valid option!")

    @classmethod
    def prompt_for_user_name(cls):
        name = input("What's your name? ")
        return name

    @classmethod
    def prompt_for_user_action(cls):
        print("Options:")
        print("  Attack: a")
        print("  Magic: m")
        print("  Defend: d")
        print("  Heal: h")

        action = input("What will you do? ")
        print(f"you chose {action}!")

        return action
