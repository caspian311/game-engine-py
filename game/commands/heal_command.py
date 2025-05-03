from game.commands.command import Command
from game.game_engine import GameEngine
from game.data import DATA

class HealCommand(Command):
    def execute(self, arguments):
        player = arguments[0]

        player.increase_health(GameEngine.HEAL_AMOUNT)

        DATA.latest_message = (
                f"{player.name()} heals by {GameEngine.HEAL_AMOUNT}!")
