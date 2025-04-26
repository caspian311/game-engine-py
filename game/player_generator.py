from faker import Factory

from game.console_manager import ConsoleManager
from game.npc_player import NpcPlayer
from game.user_player import UserPlayer

fake = Factory.create()

class PlayerGenerator():
    @classmethod
    def generate_user_player(cls):
        name = ConsoleManager.prompt_for_user_name()
        return UserPlayer(name)

    @classmethod
    def generate_npc_player(cls):
        name = fake.first_name() # pylint: disable=no-member
        return NpcPlayer(name)
