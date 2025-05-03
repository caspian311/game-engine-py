from game.monitors.battle_monitor import BattleMonitor
from game.data import DATA, GameState
from game.player import Player
from game.player_generator import PlayerGenerator

# def test_during_battle_player_goes_first():
#     test_object = BattleMonitor()
#
#     DATA.user = Player("user 1")
#     DATA.clear_npcs()
#     goblin1 = PlayerGenerator.generate_goblin_player()
#     DATA.add_npc(goblin1)
#
#     test_object.refresh()
#
#     assert False


def test_during_battle_vitory_no_baddies_left():
    test_object = BattleMonitor()

    DATA.user = Player("user 1")
    DATA.clear_npcs()

    DATA.state.run_state = GameState.IN_BATTLE

    test_object.refresh()

    assert GameState.VICTORY == DATA.state.run_state

def test_during_battle_defeat_user_has_no_more_health():
    test_object = BattleMonitor()

    DATA.user = Player("user 1")
    DATA.clear_npcs()
    DATA.add_npc(PlayerGenerator.generate_goblin_player())

    DATA.user.override_current_health(0)

    DATA.state.run_state = GameState.IN_BATTLE

    test_object.refresh()

    assert GameState.DEFEAT == DATA.state.run_state
