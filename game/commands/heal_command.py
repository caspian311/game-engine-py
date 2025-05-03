from game.commands.command import Command
from game.game_engine import GameEngine

class HealCommand(Command):
    def execute(self, arguments):
        player = arguments[0]

        player.increase_health(GameEngine.HEAL_AMOUNT)
