from game.data import DATA
from game.commands.commands import CommandProcessor, Commands

class Battle():
    def __init__(self):
        self._current_turn = 0

    def take_turn(self):
        self._current_turn = self._current_turn % len(self._turn_order())
        current_turn = self._turn_order()[self._current_turn]
        if current_turn.is_user():
            target = DATA.live_npcs()[0] if len(DATA.live_npcs()) > 0 else None
        else:
            target = DATA.user

        if "a" == current_turn.turn():
            CommandProcessor.queue_command(
                    Commands.PHYSICAL_ATTACK, [current_turn, target])
            if current_turn.is_user():
                current_turn.set_turn(None)
            return True
        if "m" == current_turn.turn():
            CommandProcessor.queue_command(
                    Commands.MAGIC_ATTACK, [current_turn, target])
            if current_turn.is_user():
                current_turn.set_turn(None)
            return True
        if "d" == current_turn.turn():
            CommandProcessor.queue_command(Commands.DEFEND, [DATA.user])
            if current_turn.is_user():
                current_turn.set_turn(None)
            return True
        if "h" == current_turn.turn():
            CommandProcessor.queue_command(Commands.HEAL, [DATA.user])
            if current_turn.is_user():
                current_turn.set_turn(None)
            return True

        return False

    def go_to_next_turn(self):
        self._current_turn += 1

    def _turn_order(self):
        turn_order = [DATA.user]
        turn_order += DATA.live_npcs()
        return turn_order
