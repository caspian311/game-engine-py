from game.create_user_command import CreateUserCommand
from game.data import DATA

def test_create_user_command_creates_user():
    assert None is DATA.user

    CreateUserCommand().execute(["test 123"])

    assert "test 123" == DATA.user.name()

def test_create_user_command_stops_prompting_for_user():
    DATA.state.prompt_for_user = True

    CreateUserCommand().execute(["test 123"])

    assert not DATA.state.prompt_for_user
