from game.player import Player

class UserPlayer(Player):
    MIN_ATTACK = 6
    MAX_ATTACK = 10
    MIN_MAGIC = 8
    MAX_MAGIC = 20
    MIN_DEFENSE = 1
    MAX_DEFENSE = 5
    MIN_CONSTITUTION = 1
    MAX_CONSTITUTION = 5

    def is_user(self):
        return True
