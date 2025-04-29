from faker import Factory

from game.npc_player import NpcPlayer, GoblinPlayer
from game.user_player import UserPlayer

fake = Factory.create()

class PlayerGenerator():
    @classmethod
    def generate_user_player(cls, name):
        return UserPlayer(name)

    @classmethod
    def generate_npc_player(cls):
        name = fake.first_name() # pylint: disable=no-member
        return NpcPlayer(name)

    @classmethod
    def generate_goblin_player(cls):
        name = fake.first_name() # pylint: disable=no-member
        return GoblinPlayer(name)
