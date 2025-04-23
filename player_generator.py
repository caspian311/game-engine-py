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
    MIN_MAGIC = 5
    MAX_MAGIC = 20

    def generate_user_player():
        name = ConsoleManager.prompt_for_user_name()
        max_health = random.randint(PlayerGenerator.MIN_HEALTH, PlayerGenerator.MAX_HEALTH)
        attack = random.randint(PlayerGenerator.MIN_ATTACK, PlayerGenerator.MAX_ATTACK)
        magic = random.randint(PlayerGenerator.MIN_MAGIC, PlayerGenerator.MAX_MAGIC)
        return UserPlayer(name, max_health, attack, magic)

    def generate_npc_player():
        name = fake.first_name()
        max_health = random.randint(PlayerGenerator.MIN_HEALTH, PlayerGenerator.MAX_HEALTH)
        attack = random.randint(PlayerGenerator.MIN_ATTACK, PlayerGenerator.MAX_ATTACK)
        magic = random.randint(PlayerGenerator.MIN_MAGIC, PlayerGenerator.MAX_MAGIC)
        return NpcPlayer(name, max_health, attack, magic)

