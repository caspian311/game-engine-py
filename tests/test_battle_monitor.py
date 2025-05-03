import mock

from game.battle_monitor import BattleMonitor
from game.commands.commands import Commands, CommandProcessor
from game.data import DATA
from game.player import Player
from game.player_generator import PlayerGenerator

@mock.patch.object(CommandProcessor, "queue_command")
def test_during_battle_player_goes_first(mock_queue_command):
    test_object = BattleMonitor()

    DATA.user = Player("user 1")
    DATA.add_npc(PlayerGenerator.generate_goblin_player())

    test_object.refresh()

    mock_queue_command.assert_called_once_with(
            Commands.PHYSICAL_ATTACK, [DATA.user, DATA.live_npcs()[0]])
