from game.data import DATA
from game.commands.command import Command
from game.player_generator import PlayerGenerator

class CreateUserCommand(Command):
    def execute(self, arguments):
        player_name = arguments[0]
        player_attack = arguments[1]
        player_defense = arguments[2]
        player_magic = arguments[3]
        player_constitution = arguments[4]

        DATA.user = PlayerGenerator.generate_user_player(player_name)
        DATA.user.override_attack(player_attack)
        DATA.user.override_defense(player_defense)
        DATA.user.override_magic(player_magic)
        DATA.user.override_constitution(player_constitution)
