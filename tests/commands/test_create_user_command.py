from game.commands.create_user_command import CreateUserCommand
from game.data import DATA

def test_create_user_command_creates_user():
    DATA.user = None

    CreateUserCommand().execute(["test 123"])

    assert "test 123" == DATA.user.name()

def test_create_user_command_creates_user_with_given_attributes():
    DATA.user = None

    CreateUserCommand().execute(["test 123", 1, 2, 3, 4])

    assert 1 == DATA.user.attack()
    assert 2 == DATA.user.defense()
    assert 3 == DATA.user.magic()
    assert 4 == DATA.user.constitution()
