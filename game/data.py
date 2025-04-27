from dataclasses import dataclass

@dataclass
class GameState():
    running = True
    prompt_for_user = True
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
