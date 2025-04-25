import random

class Player():
    MIN_HEALTH = 50
    MAX_HEALTH = 100
    MIN_ATTACK = 1
    MAX_ATTACK = 10
    MIN_MAGIC = 5
    MAX_MAGIC = 20
    MIN_DEFENSE = 1
    MAX_DEFENSE = 5
    MIN_CONSTITUTION = 1
    MAX_CONSTITUTION = 5

    def __init__(self, name):
        self._name = name

        self._max_health = random.randint(
                Player.MIN_HEALTH, Player.MAX_HEALTH)
        self._current_health = self._max_health
        self._attack = random.randint(Player.MIN_ATTACK, Player.MAX_ATTACK)
        self._magic = random.randint(Player.MIN_MAGIC, Player.MAX_MAGIC)
        self._defense = random.randint(Player.MIN_DEFENSE, Player.MAX_DEFENSE)
        self._constitution = random.randint(
                Player.MIN_CONSTITUTION, Player.MAX_CONSTITUTION)
        self._is_defending = False

    def override_constitution(self, val):
        self._constitution = val

    def constitution(self):
        return self._constitution

    def override_defense(self, val):
        self._defense = val

    def defense(self):
        return self._defense

    def override_attack(self, val):
        self._attack = val

    def attack(self):
        return self._attack

    def magic(self):
        return self._magic

    def override_magic(self, val):
        self._magic = val

    def name(self):
        return self._name

    def override_current_health(self, val):
        self._current_health = val

    def current_health(self):
        return self._current_health

    def override_max_health(self, val):
        self._max_health = val

    def max_health(self):
        return self._max_health

    def reduce_health(self, val):
        self._current_health -= val if not self._is_defending else val / 2
        self._current_health = max(self._current_health, 0)
        self._is_defending = False

    def increase_health(self, val):
        self._current_health += val

    def defend(self):
        self._is_defending = True

    def is_dead(self):
        return self._current_health == 0

    def take_turn(self, game):
        pass

    def is_user(self):
        return False
