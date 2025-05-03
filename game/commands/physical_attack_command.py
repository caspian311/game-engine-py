from game.commands.command import Command

class PhysicalAttackCommand(Command):
    def execute(self, arguments):
        attacker, defender = arguments

        damage_dealt = attacker.attack() - defender.defense()
        damage_dealt = max(damage_dealt, 0)
        defender.reduce_health(damage_dealt)
