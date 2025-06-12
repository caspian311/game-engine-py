from game.commands.command import Command
from game.data import DATA
from game.movement import Movement

class MoveUserCommand(Command):
    def execute(self, arguments):
        movement = arguments

        current_location_x, current_location_y = DATA.location_in_dungeon

        new_location_x = current_location_x
        new_location_y = current_location_y

        if movement == Movement.UP:
            new_location_y = new_location_y + 1
        elif movement == Movement.DOWN:
            new_location_y = new_location_y - 1
        elif movement == Movement.LEFT:
            new_location_x = new_location_x - 1
        elif movement == Movement.RIGHT:
            new_location_x = new_location_x + 1

        DATA.location_in_dungeon = new_location_x, new_location_y
