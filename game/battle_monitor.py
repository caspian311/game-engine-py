from game.data import DATA, GameState
from game.commands.commands import Commands, CommandProcessor

class BattleMonitor:
    def __init__(self):
        pass

    def refresh(self):
        if self._battle_in_progress():
            turn = DATA.battle.next_turn()
            turn.take_turn()

            baddie = DATA.live_npcs()[0]
            user = DATA.user
            CommandProcessor.queue_command(Commands.PHYSICAL_ATTACK, [baddie, user])

        if self._user_won_battle():
            DATA.state.run_state = GameState.VICTORY

        if self._user_lost_battle():
            DATA.state.run_state = GameState.DEFEAT

    def _battle_in_progress(self):
        return DATA.state.run_state == GameState.IN_BATTLE and len(DATA.live_npcs()) > 0

    def _user_won_battle(self):
        return DATA.state.run_state == GameState.IN_BATTLE and len(DATA.live_npcs()) == 0

    def _user_lost_battle(self):
        return DATA.state.run_state == GameState.IN_BATTLE and DATA.user.is_dead()

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
