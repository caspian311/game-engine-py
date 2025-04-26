import random

from console_manager import ConsoleManager

class GameEngine():
    MIN_ATTACK_DAMAGE = 1
    MIN_MAGIC_ATTACK_DAMAGE = 5
    HEAL_AMOUNT = 2

    @classmethod
    def attack(cls, attacker, defender):
        damage_delt = attacker.attack() - defender.defense()
        defender.reduce_health(damage_delt)

        ConsoleManager.attack_results(attacker.name(), defender.name(), damage_delt)

    @classmethod
    def heal(cls, player):
        amount = GameEngine.HEAL_AMOUNT
        print(f"{player.name()} heals for {amount} health!")
        player.increase_health(amount)

    @classmethod
    def magic_attack(cls, attacker, defender):
        min_val = GameEngine.MIN_MAGIC_ATTACK_DAMAGE
        max_val = GameEngine.MIN_MAGIC_ATTACK_DAMAGE + attacker.attack()
        damage_delt = random.randint(min_val, max_val)

        print((
            f"{attacker.name()} attacks {defender.name()} "
            f"with MAGIC and does {damage_delt} damage!"
            ))
        defender.reduce_health(damage_delt)
