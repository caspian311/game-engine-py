from dataclasses import dataclass

@dataclass
class GameState():
    QUITTING = -1
    INIT = 0
    STARTING = 1
    TITLE_PAGE = 2
    USER_CREATION = 3
    IN_BATTLE = 4
    VICTORY = 5
    DEFEAT = 6

    run_state = INIT

class BattleState():
    def __init__(self):
        self._last_turn = None

    def next_turn(self):
        if self._user_turn() is None:
            self._last_turn = self._user_turn()
            return self._last_turn

        if self._last_turn.is_user():
            return self._npc_turn()
        return self._user_turn()

    def _user_turn(self):
        return Turn()

    def _npc_turn(self):
        return Turn()

class Turn():
    def is_user(self):
        return True

    def take_turn(self):
        pass

@dataclass
class Data():
    window = {
        "width": 240,
        "height": 55
    }
    state = GameState()
    user = None
    battle = BattleState()
    _npcs = []

    @classmethod
    def add_npc(cls, player):
        cls._npcs.append(player)

    @classmethod
    def live_npcs(cls):
        return [npc for npc in cls._npcs if not npc.is_dead()]

    @classmethod
    def clear_npcs(cls):
        cls._npcs = []

DATA = Data()
