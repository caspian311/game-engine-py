import random

class GameEngine():
    MIN_ATTACK_DAMAGE = 1

    def __init__(self):
        self._players = []

    def add_player(self, player):
        self._players.append(player)

    def players(self):
        return self._players

    def attack(self, player1, player2):
        damage_delt = random.randint(GameEngine.MIN_ATTACK_DAMAGE, player1.strength())

        print(f"{player1.name()} attacks {player2.name()} and does {damage_delt} damage!")
        player2.reduce_health(damage_delt)

    def heal(self, player, amount):
        print(f"{player.name()} heals for {amount} health!")
        player.increase_health(amount)
