from game.data import DATA
from game.command import Command
from game.player_generator import PlayerGenerator

class CreateUserCommand(Command):
    def execute(self, arguments):
        player_name = arguments[0]

        DATA.user = PlayerGenerator.generate_user_player(player_name)
