
def calculate_player_position(middle_of_window_width, middle_of_window_height,
                              fighter_standing_content):
    return (_calculate_player_width(middle_of_window_width, fighter_standing_content),
            _calculate_player_height(middle_of_window_height, fighter_standing_content))

def _calculate_player_width(middle_of_window_width, fighter_standing_content):
    player_width = len(fighter_standing_content[0])
    middle_of_player = int(player_width / 2)
    quarter_of_window = int(middle_of_window_width / 2)
    start_of_player = quarter_of_window - middle_of_player
    return start_of_player

def _calculate_player_height(middle_of_window_height, fighter_standing_content):
    player_height = len(fighter_standing_content)
    middle_of_player = int(player_height / 2)
    start_of_player = middle_of_window_height - middle_of_player
    return start_of_player
