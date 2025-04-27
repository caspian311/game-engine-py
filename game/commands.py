from game.game_engine import GameEngine
from game.logger import log
from game.data import DATA
from game.user_player import UserPlayer

class Command():
    def execute(self, arguments):
        pass

class StartCommand(Command):
    def execute(self, arguments):
        DATA.state.running = True
        DATA.state.prompt_for_user = True

class CreateUserCommand(Command):
    def execute(self, arguments):
        player_name = arguments[0]

        DATA.user = UserPlayer(player_name)
        DATA.prompt_for_user = False

class QuitCommand(Command):
    def execute(self, arguments):
        DATA.state.running = False

class PhysicalAttackCommand(Command):
    def execute(self, arguments):
        attacker, defender = arguments

        damage_dealt = attacker.attack() - defender.defense()
        defender.reduce_health(damage_dealt)

class MagicAttackCommand(Command):
    def execute(self, arguments):
        attacker, defender = arguments

        damage_dealt = attacker.magic() - defender.constitution()
        defender.reduce_health(damage_dealt)

class DefendCommand(Command):
    def execute(self, arguments):
        player = arguments[0]

        player.defend()

class HealCommand(Command):
    def execute(self, arguments):
        player = arguments[0]

        player.increase_health(GameEngine.HEAL_AMOUNT)

class Commands():
    START = "START"
    CREATE_USER = "CREATE_USER"
    QUIT = "QUIT"
    PHYSICAL_ATTACK = "PHYSICAL_ATTACK"
    MAGIC_ATTACK = "MAGIC_ATTACK"
    DEFEND = "DEFEND"
    HEAL = "HEAL"

    all_commands = {
        START: StartCommand(),
        CREATE_USER: CreateUserCommand(),
        QUIT: QuitCommand(),
        PHYSICAL_ATTACK: PhysicalAttackCommand(),
        MAGIC_ATTACK: MagicAttackCommand(),
        DEFEND: DefendCommand(),
        HEAL: HealCommand()
    }

    @classmethod
    def execute(cls, command, arguments):
        if command in cls.all_commands:
            cls.all_commands[command].execute(arguments)
        else:
            log(f"invalid command received: {command}")
