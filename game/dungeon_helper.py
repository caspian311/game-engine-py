dungeon_content = []
with open("./dungeons/dungeon01.txt", "r", encoding="UTF-8") as file:
    for line in file:
        split_line = list(line.rstrip().lstrip())
        dungeon_content.append(split_line)

def dungeon_map():
    return dungeon_content

def player_position_in_dungeon():
    for y in range(0, len(dungeon_map())):
        for x in range(0, len(dungeon_map()[y])):
            if dungeon_map()[y][x] == "*":
                return x, y
    return 0, 0

def player_surroundings():
    dungeon_height = len(dungeon_map())
    dungeon_width = len(dungeon_map()[0])

    player_x, player_y = player_position_in_dungeon()

    start_x = max(player_x - 5, 0)
    end_x = min(player_x + 6, dungeon_width)

    start_y = max(player_y - 5, 0)
    end_y = min(player_y + 6, dungeon_height)

    ret_val = []
    lines = dungeon_map()[start_y:end_y]

    for ret_line in lines:
        ret_val.append(ret_line[start_x:end_x])

    return ret_val

def blow_up_player_surroundings(width, height):
    player_surr = player_surroundings()
    height_of_player_surroundings = len(player_surr)
    height_scale_factor = int(height_of_player_surroundings / height)

    width_of_player_surroundings = len(player_surr[0])
    width_scale_factor = int(width_of_player_surroundings / height)

    ret_val = [[" " for x in range(width)] for y in range(height)]

    for y, _ in enumerate(player_surr):
        for x, _ in enumerate(player_surr[y]):
            character = player_surr[y][x]
            if character == "-":
                x_offset_start = 0
                y_offset_start = 0
                x_offset_range = 0
                y_offset_range = 0

                for i in range(y_offset_start, y_offset_range):
                    for j in range(x_offset_start, x_offset_range):
                        ret_val[i][j] = "-"
            elif character == "|":
                pass



    return ret_val
