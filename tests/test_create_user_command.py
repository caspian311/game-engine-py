from game.create_user_command import CreateUserCommand
from game.data import DATA

def test_create_user_command_creates_user():
    assert None is DATA.user

    CreateUserCommand().execute(["test 123"])

    assert "test 123" == DATA.user.name()
