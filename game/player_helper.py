fighter_standing_content = []
with open("./artwork/fighter_standing.txt", "r", encoding="UTF-8") as file:
    for line in file:
        fighter_standing_content.append(line)

def calculate_player_position(middle_of_window_width, middle_of_window_height):
    return (_calculate_player_width(middle_of_window_width),
            _calculate_player_height(middle_of_window_height))

def _calculate_player_width(middle_of_window_width):
    player_width = len(fighter_standing_content[0])
    middle_of_player = int(player_width / 2)
    quarter_of_window = int(middle_of_window_width / 2)
    start_of_player = quarter_of_window - middle_of_player
    return start_of_player

def _calculate_player_height(middle_of_window_height):
    player_height = len(fighter_standing_content)
    middle_of_player = int(player_height / 2)
    start_of_player = middle_of_window_height - middle_of_player
    return start_of_player


def fighter_standing():
    return fighter_standing_content
