from game.command import Command

class MagicAttackCommand(Command):
    def execute(self, arguments):
        attacker, defender = arguments

        damage_dealt = attacker.magic() - defender.constitution()
        defender.reduce_health(damage_dealt)
