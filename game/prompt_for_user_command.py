from game.command import Command
from game.data import DATA

class PromptForUserCommand(Command):
    def execute(self, arguments):
        DATA.state.prompt_for_user = True
