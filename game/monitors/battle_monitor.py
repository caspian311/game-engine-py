from game.data import DATA, GameState
from game.commands.commands import Commands, CommandProcessor
from game.logger import log

class BattleMonitor:
    def __init__(self):
        self._battle = None

    def refresh(self):
        if self._battle_in_progress():
            turn = self._current_battle().next_turn()
            turn.take_turn()

#            baddie = DATA.live_npcs()[0]
#            user = DATA.user
#            CommandProcessor.queue_command(Commands.PHYSICAL_ATTACK, [baddie, user])

        if self._user_won_battle():
            self._clear_battle()
            DATA.state.run_state = GameState.VICTORY

        if self._user_lost_battle():
            self._clear_battle()
            DATA.state.run_state = GameState.DEFEAT

    def _clear_battle(self):
        self._battle = None

    def _current_battle(self):
        self._battle = self._battle if self._battle is not None else Battle()
        return self._battle

    def _battle_in_progress(self):
        return DATA.state.run_state == GameState.IN_BATTLE and len(DATA.live_npcs()) > 0

    def _user_won_battle(self):
        return DATA.state.run_state == GameState.IN_BATTLE and len(DATA.live_npcs()) == 0

    def _user_lost_battle(self):
        return DATA.state.run_state == GameState.IN_BATTLE and DATA.user.is_dead()

class Battle():
    def __init__(self):
        self._current_turn = 0
        self._turn_order = [DATA.user]
        self._turn_order += DATA.live_npcs()

    def next_turn(self):
        current_turn = self._turn_order[self._current_turn]
        self._current_turn += 1
        self._current_turn = self._current_turn % len(self._turn_order)

        log(f"current turn: {current_turn}")

        return Turn(current_turn)

class Turn():
    def __init__(self, player):
        self._player = player

    def is_user(self):
        return self._player.is_user()

    def take_turn(self):
        pass

# class PlayerIterator:
#     def __init__(self):
#         pass
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if len(DATA.live_npcs) == 0:
#             raise StopIteration
#
#         return Player("")
