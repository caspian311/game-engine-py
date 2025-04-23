import random
from faker import Factory
fake = Factory.create()

from console_manager import ConsoleManager
from npc_player import NpcPlayer
from user_player import UserPlayer

class PlayerGenerator():
    MIN_HEALTH = 50
    MAX_HEALTH = 100
    MIN_ATTACK = 1
    MAX_ATTACK = 10

    def generate_user_player():
        name = ConsoleManager.prompt_for_user_name()
        max_health = random.randint(PlayerGenerator.MIN_HEALTH, PlayerGenerator.MAX_HEALTH)
        attack = random.randint(PlayerGenerator.MIN_ATTACK, PlayerGenerator.MAX_ATTACK)
        return UserPlayer(name, max_health, attack)

    def generate_npc_player():
        name = fake.first_name()
        max_health = random.randint(PlayerGenerator.MIN_HEALTH, PlayerGenerator.MAX_HEALTH)
        attack = random.randint(PlayerGenerator.MIN_ATTACK, PlayerGenerator.MAX_ATTACK)
        return NpcPlayer(name, max_health, attack)

