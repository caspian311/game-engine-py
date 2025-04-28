from dataclasses import dataclass

@dataclass
class GameState():
    RUN_STATE_INIT = 0
    RUN_STATE_STARTING = 1
    RUN_STATE_RUNNING = 2
    RUN_STATE_QUITTING = 3
    
    run_state = RUN_STATE_INIT
    prompt_for_user = False
    in_battle = False
    show_victory = False

@dataclass
class Data():
    state = GameState()
    user = None
    _npcs = []

    @classmethod
    def add_npc(cls, player):
        cls._npcs.append(player)

    @classmethod
    def live_npcs(cls):
        return [npc for npc in cls._npcs if not npc.is_dead()]

DATA = Data()
