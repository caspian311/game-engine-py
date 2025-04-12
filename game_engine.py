import random

class GameEngine():
    MIN_ATTACK_DAMAGE = 1
    HEAL_AMOUNT = 2

    def __init__(self):
        self._players = []
        self._npcs = []

    def add_player(self, player):
        self._players.append(player)

    def add_npc(self, player):
        self._npcs.append(player)

    def all_players(self):
        return self._players + self._npcs

    def all_npcs(self):
        return self._npcs

    def attack(self, player1, player2):
        damage_delt = random.randint(GameEngine.MIN_ATTACK_DAMAGE, player1.strength())

        print(f"{player1.name()} attacks {player2.name()} and does {damage_delt} damage!")
        player2.reduce_health(damage_delt)

    def heal(self, player):
        amount = GameEngine.HEAL_AMOUNT
        print(f"{player.name()} heals for {amount} health!")
        player.increase_health(amount)
