class Player():
    def __init__(self, name, max_health, strength):
        self._name = name
        self._max_health = max_health
        self._current_health = max_health
        self._strength = strength

    def print_stats(self):
        print(f"Name: {self._name}\n  health: {self._current_health}/{self._max_health}\n  strength: {self._strength}")
