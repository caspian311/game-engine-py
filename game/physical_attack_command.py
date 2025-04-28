from game.command import Command

class PhysicalAttackCommand(Command):
    def execute(self, arguments):
        attacker, defender = arguments

        damage_dealt = attacker.attack() - defender.defense()
        defender.reduce_health(damage_dealt)
