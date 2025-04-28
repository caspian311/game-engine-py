from game.command import Command

class DefendCommand(Command):
    def execute(self, arguments):
        player = arguments[0]

        player.defend()
