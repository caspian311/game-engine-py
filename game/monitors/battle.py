from game.data import DATA

class Battle():
    def __init__(self):
        self._current_turn = 0
        self._turn_order = [DATA.user]
        self._turn_order += DATA.live_npcs()

    def next_turn(self):
        current_turn = self._turn_order[self._current_turn]
        self._current_turn += 1
        self._current_turn = self._current_turn % len(self._turn_order)

        return current_turn
