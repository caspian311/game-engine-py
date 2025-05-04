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

@dataclass
class UserTemplate():
    select_attribute_index = 0
    remaining_points = 5

    name = None
    attack = 5
    defense = 5
    magic = 5
    constitution = 5

@dataclass
class Data():
    window = {
        "width": 240,
        "height": 55
    }
    state = GameState()
    user = None
    _npcs = []
    latest_message = None
    temp_user = UserTemplate()

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
