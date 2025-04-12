import random
from faker import Factory
fake = Factory.create()

from player import Player

class PlayerGenerator():
    MIN_HEALTH = 50
    MAX_HEALTH = 100
    MIN_STRENGTH = 1
    MAX_STRENGTH = 10

    def generate_player(name=fake.first_name()):
        max_health = random.randint(PlayerGenerator.MIN_HEALTH, PlayerGenerator.MAX_HEALTH)
        strength = random.randint(PlayerGenerator.MIN_STRENGTH, PlayerGenerator.MAX_STRENGTH)
        return Player(name, max_health, strength)

