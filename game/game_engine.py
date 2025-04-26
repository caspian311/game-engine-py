from game.console_manager import ConsoleManager

class GameEngine():
    MIN_ATTACK_DAMAGE = 1
    MIN_MAGIC_ATTACK_DAMAGE = 5
    HEAL_AMOUNT = 2

    @classmethod
    def attack(cls, attacker, defender):
        damage_delt = attacker.attack() - defender.defense()
        defender.reduce_health(damage_delt)

        ConsoleManager.attack_results(attacker.name(), defender.name(), damage_delt)

    @classmethod
    def heal(cls, player):
        player.increase_health(GameEngine.HEAL_AMOUNT)

        ConsoleManager.heal_results(player.name(), GameEngine.HEAL_AMOUNT)

    @classmethod
    def magic_attack(cls, attacker, defender):
        damage_delt = attacker.magic() - defender.constitution()

        defender.reduce_health(damage_delt)
        ConsoleManager.magic_attack_results(attacker.name(), defender.name(), damage_delt)
