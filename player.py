class Player():
    def __init__(self, name, max_health, strength):
        self._name = name
        self._max_health = max_health
        self._current_health = max_health
        self._strength = strength

    def print_stats(self):
        print(f"Name: {self._name} ({self._strength}) {self._health_progress_bar(20)} ({self._current_health}/{self._max_health})")

    def _health_progress_bar(self, scale):
        percent_health_remaining = (self._current_health / self._max_health)
        health_scaled = int(percent_health_remaining * scale)

        lost_health_val = scale - health_scaled
        remaining_health_val = scale - lost_health_val

        lost_health = "-" * lost_health_val
        remaining_health = "#" * remaining_health_val
        percent_health = int(percent_health_remaining * 100)

        return f"{lost_health}{remaining_health}"

    def reduce_health(self, val):
        self._current_health -= val

