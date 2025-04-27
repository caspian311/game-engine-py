from time import sleep

from game.commands import Commands
from game.data import DATA

class CommandProcessor():
    commands = []

    @classmethod
    def process(cls):
        while DATA.state.running:
            if len(cls.commands) != 0:
                next_command, arguments = cls.commands.pop(0)
                Commands.execute(next_command, arguments)
            sleep(.1)

    @classmethod
    def queue_command(cls, command, arguments):
        cls.commands.append((command, arguments))
