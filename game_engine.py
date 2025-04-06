
class GameEngine():

    def attack(self, player1, player2):
        player1.reduce_health(10)
        player2.reduce_health(20)

