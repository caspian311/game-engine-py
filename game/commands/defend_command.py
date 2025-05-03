from game.commands.command import Command
from game.data import DATA

class DefendCommand(Command):
    def execute(self, arguments):
        player = arguments[0]

        player.defend()

        DATA.latest_message = (
                f"{player.name()} defends!")
