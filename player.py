class Player():
    def __init__(self, name, max_health, attack, magic, defense, constitution):
        self._name = name
        self._max_health = max_health
        self._current_health = max_health
        self._attack = attack
        self._magic = magic
        self._defense = defense
        self._constitution = constitution
        self._is_defending = False

    def constitution(self):
        return self._constitution

    def defense(self):
        return self._defense

    def attack(self):
        return self._attack

    def magic(self):
        return self._magic

    def name(self):
        return self._name

    def current_health(self):
        return self._current_health

    def max_health(self):
        return self._max_health

    def reduce_health(self, val):
        self._current_health -= val if not self._is_defending else val / 2
        if self._current_health < 0:
            self._current_health = 0
        self._is_defending = False

    def increase_health(self, val):
        self._current_health += val

    def defend(self):
        self._is_defending = True

    def is_dead(self):
        return self._current_health == 0

    def take_turn(self, target):
        pass

    def is_user(self):
        return False
