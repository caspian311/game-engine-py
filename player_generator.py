from player import Player

class PlayerGenerator():
    num_players = 0

    def generate_player():
        PlayerGenerator.num_players += 1
        name = f"Player {PlayerGenerator.num_players}"
        max_health = 100
        strength = 5
        return Player(name, max_health, strength)

