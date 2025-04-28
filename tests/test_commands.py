from game.commands import Commands, CommandProcessor
from game.start_command import StartCommand

def test_initially_no_commands_queued():
    assert 0 == len(CommandProcessor.commands)

def test_queue_command_adds():
    CommandProcessor.queue_command(StartCommand(), [])

    assert 1 == len(CommandProcessor.commands)
