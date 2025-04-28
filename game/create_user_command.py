from game.data import DATA
from game.user_player import UserPlayer
from game.command import Command

class CreateUserCommand(Command):
    def execute(self, arguments):
        player_name = arguments[0]

        DATA.user = UserPlayer(player_name)
        DATA.state.prompt_for_user = False
