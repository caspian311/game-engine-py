from time import sleep

from game.data import DATA, GameState
from game.logger import log
from game.commands.start_command import StartCommand
from game.commands.start_battle_command import StartBattleCommand
from game.commands.create_user_command import CreateUserCommand
from game.commands.win_battle_command import WinBattleCommand
from game.commands.lose_battle_command import LoseBattleCommand
from game.commands.quit_command import QuitCommand
from game.commands.physical_attack_command import PhysicalAttackCommand
from game.commands.magic_attack_command import MagicAttackCommand
from game.commands.defend_command import DefendCommand
from game.commands.heal_command import HealCommand
from game.commands.title_page_command import ShowTitlePageCommand, HideTitlePageCommand

class Commands():
    START = "START"
    START_BATTLE = "START_BATTLE"
    SHOW_TITLE_PAGE = "SHOW_TITLE_PAGE"
    HIDE_TITLE_PAGE = "HIDE_TITLE_PAGE"
    CREATE_USER = "CREATE_USER"
    QUIT = "QUIT"
    PHYSICAL_ATTACK = "PHYSICAL_ATTACK"
    MAGIC_ATTACK = "MAGIC_ATTACK"
    DEFEND = "DEFEND"
    HEAL = "HEAL"
    WIN_BATTLE = "WIN_BATTLE"
    LOSE_BATTLE = "LOSE_BATTLE"

    all_commands = {
        START: StartCommand(),
        START_BATTLE: StartBattleCommand(),
        SHOW_TITLE_PAGE: ShowTitlePageCommand(),
        HIDE_TITLE_PAGE: HideTitlePageCommand(),
        CREATE_USER: CreateUserCommand(),
        QUIT: QuitCommand(),
        PHYSICAL_ATTACK: PhysicalAttackCommand(),
        MAGIC_ATTACK: MagicAttackCommand(),
        DEFEND: DefendCommand(),
        HEAL: HealCommand(),
        WIN_BATTLE: WinBattleCommand(),
        LOSE_BATTLE: LoseBattleCommand()
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
        while DATA.state.run_state != GameState.QUITTING:
            if len(cls.commands) != 0:
                next_command, arguments = cls.commands.pop(0)
                Commands.execute(next_command, arguments)
            sleep(.1)

    @classmethod
    def queue_command(cls, command, arguments):
        cls.commands.append((command, arguments))
