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

    print(f"player position: {player_x}, {player_y}")

    start_x = max(player_x - 5, 0)
    end_x = min(player_x + 6, dungeon_width)

    print(f"x range: {start_x}:{end_x}")

    start_y = max(player_y - 5, 0)
    end_y = min(player_y + 6, dungeon_height)

    print(f"y range: {start_y}:{end_y}")

    ret_val = []
    lines = dungeon_map()[start_y:end_y]

    for ret_line in lines:
        ret_val.append(ret_line[start_x:end_x])

    return ret_val
