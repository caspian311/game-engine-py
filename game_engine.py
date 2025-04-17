import random

class GameEngine():
    MIN_ATTACK_DAMAGE = 1
    MIN_MAGIC_ATTACK_DAMAGE = 5
    HEAL_AMOUNT = 2

    def attack(attacker, defender):
        min = GameEngine.MIN_ATTACK_DAMAGE
        max = attacker.strength()
        damage_delt = random.randint(min, max)

        print(f"{attacker.name()} attacks {defender.name()} and does {damage_delt} damage!")
        defender.reduce_health(damage_delt)

    def heal(player):
        amount = GameEngine.HEAL_AMOUNT
        print(f"{player.name()} heals for {amount} health!")
        player.increase_health(amount)

    def magic_attack(attacker, defender):
        min = GameEngine.MIN_MAGIC_ATTACK_DAMAGE
        max = GameEngine.MIN_MAGIC_ATTACK_DAMAGE + attacker.strength()
        damage_delt = random.randint(min, max)

        print(f"{attacker.name()} attacks {defender.name()} with MAGIC and does {damage_delt} damage!")
        defender.reduce_health(damage_delt)
