from time import sleep

from game.game_engine import GameEngine
from game.data import DATA
from game.user_player import UserPlayer
from game.npc_player import NpcPlayer
from game.logger import log

class Command():
    def execute(self, arguments):
        pass

class StartCommand(Command):
    def execute(self, arguments):
        DATA.add_npc(NpcPlayer('Goblin 1'))
        DATA.add_npc(NpcPlayer('Goblin 2'))
        DATA.state.prompt_for_user = True
        CommandProcessor.queue_command(Commands.START_BATTLE, [])

class StartBattleCommand(Command):
    def execute(self, arguments):
        DATA.state.in_battle = True

class CreateUserCommand(Command):
    def execute(self, arguments):
        player_name = arguments[0]

        DATA.user = UserPlayer(player_name)
        DATA.state.prompt_for_user = False

class UpdateGameStateCommand(Command):
    def execute(self, arguments):
        if len(DATA.live_npcs()) == 0:
            DATA.state.in_battle = False
            DATA.state.show_victory = True

class QuitCommand(Command):
    def execute(self, arguments):
        DATA.state.running = False

class PhysicalAttackCommand(Command):
    def execute(self, arguments):
        attacker, defender = arguments

        damage_dealt = attacker.attack() - defender.defense()
        defender.reduce_health(damage_dealt)

        CommandProcessor.queue_command(Commands.UPDATE_GAME_STATE, [])

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
    START_BATTLE = "START_BATTLE"
    CREATE_USER = "CREATE_USER"
    QUIT = "QUIT"
    PHYSICAL_ATTACK = "PHYSICAL_ATTACK"
    MAGIC_ATTACK = "MAGIC_ATTACK"
    DEFEND = "DEFEND"
    HEAL = "HEAL"
    UPDATE_GAME_STATE = "UPDATE_GAME_STATE"

    all_commands = {
        START: StartCommand(),
        START_BATTLE: StartBattleCommand(),
        CREATE_USER: CreateUserCommand(),
        QUIT: QuitCommand(),
        PHYSICAL_ATTACK: PhysicalAttackCommand(),
        MAGIC_ATTACK: MagicAttackCommand(),
        DEFEND: DefendCommand(),
        HEAL: HealCommand(),
        UPDATE_GAME_STATE: UpdateGameStateCommand()
    }

    @classmethod
    def execute(cls, command, arguments):
        if command in cls.all_commands:
            log(f"executing command: {command} - with {arguments}")
            cls.all_commands[command].execute(arguments)
        else:
            log(f"invalid command received: {command}")

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
