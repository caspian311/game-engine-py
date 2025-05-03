from game.data import DATA

class Battle():
    def __init__(self):
        self._current_turn = 0

    def next_turn(self):
        self._current_turn = self._current_turn % len(self._turn_order())
        current_turn = self._turn_order()[self._current_turn]
        self._current_turn += 1

        return current_turn

    def _turn_order(self):
        turn_order = [DATA.user]
        turn_order += DATA.live_npcs()
        return turn_order
