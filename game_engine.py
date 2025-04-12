import random

class GameEngine():
    MIN_ATTACK_DAMAGE = 1

    def attack(self, player1, player2):
        damage_delt = random.randint(GameEngine.MIN_ATTACK_DAMAGE, player1.strength())

        print(f"{player1.name()} attacks {player2.name()} and does {damage_delt} damage!")
        player1.reduce_health(damage_delt)

