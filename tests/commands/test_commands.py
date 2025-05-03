from game.commands.commands import Commands, CommandProcessor
from game.commands.start_command import StartCommand
from game.data import DATA, GameState

def test_initially_no_commands_queued():
    assert 0 == len(CommandProcessor.commands)

def test_queue_command_adds():
    CommandProcessor.queue_command(StartCommand(), [])

    assert 1 == len(CommandProcessor.commands)

def test_excute_will_excute_given_command():
    DATA.state.run_state = GameState.INIT

    Commands.execute(Commands.START, [])

    assert GameState.STARTING == DATA.state.run_state

def test_excute_will_not_blow_up_if_given_bad_command():
    Commands.execute("something", [])

    assert True
