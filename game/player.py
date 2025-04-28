import random
from dataclasses import dataclass

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
        self._attributes = Attributes()

        self._is_defending = False

    def override_constitution(self, val):
        self._attributes.constitution = val

    def constitution(self):
        return self._attributes.constitution

    def override_defense(self, val):
        self._attributes.defense = val

    def defense(self):
        return self._attributes.defense

    def override_attack(self, val):
        self._attributes.attack = val

    def attack(self):
        return self._attributes.attack

    def magic(self):
        return self._attributes.magic

    def override_magic(self, val):
        self._attributes.magic = val

    def name(self):
        return self._name

    def override_current_health(self, val):
        self._attributes.current_health = val

    def current_health(self):
        return self._attributes.current_health

    def override_max_health(self, val):
        self._attributes.max_health = val

    def max_health(self):
        return self._attributes.max_health

    def reduce_health(self, val):
        self._attributes.current_health -= val if not self._is_defending else val / 2
        self._attributes.current_health = max(self._attributes.current_health, 0)
        self._is_defending = False

    def increase_health(self, val):
        self._attributes.current_health += val

    def defend(self):
        self._is_defending = True

    def is_dead(self):
        return self._attributes.current_health == 0

    def take_turn(self, game):
        pass

    def is_user(self):
        return False

@dataclass
class Attributes():
    def __init__(self):
        self.max_health = random.randint(
                Player.MIN_HEALTH, Player.MAX_HEALTH)
        self.current_health = self.max_health
        self.attack = random.randint(Player.MIN_ATTACK, Player.MAX_ATTACK)
        self.magic = random.randint(Player.MIN_MAGIC, Player.MAX_MAGIC)
        self.defense = random.randint(Player.MIN_DEFENSE, Player.MAX_DEFENSE)
        self.constitution = random.randint(
                Player.MIN_CONSTITUTION, Player.MAX_CONSTITUTION)
