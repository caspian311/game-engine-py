from game.data import DATA, GameState
from game.monitors.battle import Battle

class BattleMonitor:
    def __init__(self):
        self._battle = None

    def refresh(self):
        if self._battle_in_progress():
            battle = self._current_battle()
            if battle.take_turn():
                battle.go_to_next_turn()

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
