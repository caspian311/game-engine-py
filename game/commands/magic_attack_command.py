from game.commands.command import Command

class MagicAttackCommand(Command):
    def execute(self, arguments):
        attacker, defender = arguments

        damage_dealt = attacker.magic() - defender.constitution()
        damage_dealt = max(damage_dealt, 0)
        defender.reduce_health(damage_dealt)
