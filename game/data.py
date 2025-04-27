from dataclasses import dataclass

@dataclass
class GameState():
    running = True
    prompt_for_user = True

@dataclass
class Data():
    state = GameState()
    user = None
    npcs = []

DATA = Data()
