from game.commands.command import Command
from game.data import DATA

class MagicAttackCommand(Command):
    def execute(self, arguments):
        attacker, defender = arguments

        damage_dealt = attacker.magic() - defender.constitution()
        damage_dealt = max(damage_dealt, 0)
        defender.reduce_health(damage_dealt)

        DATA.latest_message = (
                f"{attacker.name()} attacked "
                f"{defender.name()} with MAGIC "
                f"for {damage_dealt} damage!"
                )
