class Player():
    def __init__(self, name, max_health, strength):
        self._name = name
        self._max_health = max_health
        self._current_health = max_health
        self._strength = strength

    def print_stats(self):
        print(f"Name: {self._name}\n  {self._health_progress_bar()}\n  strength: {self._strength}")

    def _health_progress_bar(self):
        SCALE = 20
        percent_health = (self._current_health / self._max_health)
        health_scaled = int(percent_health * SCALE)

        lost_health_val = SCALE - health_scaled
        remaining_health_val = SCALE - lost_health_val

        lost_health = "-" * lost_health_val
        remaining_health = "#" * remaining_health_val
        return f"{lost_health}{remaining_health} ({int(percent_health * 100)}%)"

    def reduce_health(self, val):
        self._current_health -= val

