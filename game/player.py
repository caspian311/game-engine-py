import random
from dataclasses import dataclass

class Player():
    MIN_HEALTH = 50
    MAX_HEALTH = 100
    MIN_ATTACK = 1
    MAX_ATTACK = 10
    MIN_MAGIC = 0
    MAX_MAGIC = 0
    MIN_DEFENSE = 1
    MAX_DEFENSE = 5
    MIN_CONSTITUTION = 0
    MAX_CONSTITUTION = 0

    def __init__(self, name):
        self._name = name
        self._turn = None
        self._attributes = Attributes(type(self))

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

    def is_defending(self):
        return self._is_defending

    def is_dead(self):
        return self._attributes.current_health == 0

    def is_user(self):
        return False

    def turn(self):
        pass

@dataclass
class Attributes():
    def __init__(self, parent):
        self.max_health = random.randint(
                parent.MIN_HEALTH, parent.MAX_HEALTH)
        self.current_health = self.max_health
        self.attack = random.randint(parent.MIN_ATTACK, parent.MAX_ATTACK)
        self.magic = random.randint(parent.MIN_MAGIC, parent.MAX_MAGIC)
        self.defense = random.randint(parent.MIN_DEFENSE, parent.MAX_DEFENSE)
        self.constitution = random.randint(
                parent.MIN_CONSTITUTION, parent.MAX_CONSTITUTION)
