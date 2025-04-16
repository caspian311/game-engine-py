import random
from faker import Factory
fake = Factory.create()

from console_manager import ConsoleManager
from npc_player import NpcPlayer
from user_player import UserPlayer

class PlayerGenerator():
    MIN_HEALTH = 50
    MAX_HEALTH = 100
    MIN_STRENGTH = 1
    MAX_STRENGTH = 10

    def generate_user_player():
        name = ConsoleManager.prompt_for_user_name()
        max_health = random.randint(PlayerGenerator.MIN_HEALTH, PlayerGenerator.MAX_HEALTH)
        strength = random.randint(PlayerGenerator.MIN_STRENGTH, PlayerGenerator.MAX_STRENGTH)
        return UserPlayer(name, max_health, strength)

    def generate_npc_player():
        name = fake.first_name()
        max_health = random.randint(PlayerGenerator.MIN_HEALTH, PlayerGenerator.MAX_HEALTH)
        strength = random.randint(PlayerGenerator.MIN_STRENGTH, PlayerGenerator.MAX_STRENGTH)
        return NpcPlayer(name, max_health, strength)

