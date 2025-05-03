from game.commands.command import Command
from game.data import DATA

class PhysicalAttackCommand(Command):
    def execute(self, arguments):
        attacker, defender = arguments

        damage_dealt = attacker.attack() - defender.defense()
        damage_dealt = max(damage_dealt, 0)
        defender.reduce_health(damage_dealt)

        DATA.latest_message = (
                f"{attacker.name()} attacked {defender.name()} for {damage_dealt} damage!")
