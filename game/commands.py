from time import sleep

from game.data import DATA, GameState
from game.logger import log
from game.start_command import StartCommand
from game.start_battle_command import StartBattleCommand
from game.prompt_for_user_command import PromptForUserCommand
from game.create_user_command import CreateUserCommand
from game.update_game_state_command import UpdateGameStateCommand
from game.quit_command import QuitCommand
from game.physical_attack_command import PhysicalAttackCommand
from game.magic_attack_command import MagicAttackCommand
from game.defend_command import DefendCommand
from game.heal_command import HealCommand

class Commands():
    START = "START"
    START_BATTLE = "START_BATTLE"
    PROMPT_FOR_USER = "PROMPT_FOR_USER"
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
        PROMPT_FOR_USER: PromptForUserCommand(),
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
        while DATA.state.run_state != GameState.RUN_STATE_QUITTING:
            if len(cls.commands) != 0:
                next_command, arguments = cls.commands.pop(0)
                Commands.execute(next_command, arguments)
            sleep(.1)

    @classmethod
    def queue_command(cls, command, arguments):
        cls.commands.append((command, arguments))
