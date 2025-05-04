
goblins_content = []
for f in range(3):
    with open(f"./artwork/goblins0{f+1}.txt", "r", encoding="UTF-8") as file:
        goblins_content.append([])
        for line in file:
            goblins_content[f].append(line)

def calculate_goblin_position(g, max_goblins, middle_of_window_width, window_height):
    return (_calculate_goblin_width(g, middle_of_window_width),
            _calculate_goblin_height(g, max_goblins, window_height))

def _calculate_goblin_width(g, middle_of_window_width):
    goblin_width = len(goblins_content[g])
    middle_of_goblin = int(goblin_width / 2)
    quarter_of_window = int(middle_of_window_width / 2)
    start_of_goblin = (quarter_of_window * 3) - middle_of_goblin
    return start_of_goblin

def _calculate_goblin_height(g, max_goblins, window_height):
    goblin_height = len(goblins_content[g])
    middle_of_goblin = int(goblin_height / 2)
    middle_of_window = int((window_height / (max_goblins + 1)) * (g + 1))
    start_of_goblin = middle_of_window - middle_of_goblin
    return start_of_goblin
