from game.player import Player

class GoblinPlayer(Player):
    MIN_HEALTH = 15
    MAX_HEALTH = 20
    MIN_ATTACK = 5
    MAX_ATTACK = 8

class NpcPlayer(Player):
    pass
