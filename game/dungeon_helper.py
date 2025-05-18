import numpy as np

original_dungeon_content = []
with open("./dungeons/dungeon01.txt", "r", encoding="UTF-8") as file:
    for l in file:
        split_line = list(l.rstrip().lstrip())
        original_dungeon_content.append(split_line)

def blow_up_map(mini_map, size):
    if size % 2 == 0:
        raise ValueError(f"{size} must be odd")

    file_expansion = []
    for line in mini_map:
        line_expansion = []

        for char in line:
            if char == " ":
                line_expansion.append(np.array(make_grid_for_space(size)))
            elif char == "-":
                line_expansion.append(np.array(make_grid_for_dash(size)))
            elif char == "|":
                line_expansion.append(np.array(make_grid_for_pipe(size)))

        file_expansion.append(line_expansion)

    return np.block(file_expansion)

def make_grid_for_space(size):
    grid = []
    for _ in range(0, size):
        row = []

        for _ in range(0, size):
            row.append(" ")

        grid.append(row)
    return grid

def make_grid_for_dash(size):
    grid = []
    for index in range(0, size):
        row = []

        character = " "
        if index == int(size / 2):
            character = "-"

        for _ in range(0, size):
            row.append(character)

        grid.append(row)
    return grid

def make_grid_for_pipe(size):
    grid = []
    for _ in range(0, size):
        row = []

        for index in range(0, size):
            character = " "
            if index == int(size / 2):
                character = "|"

            row.append(character)

        grid.append(row)
    return grid

def user_initial_location(map_grid):
    for y, line in enumerate(map_grid):
        for x, character in enumerate(line):
            if character == "*":
                return x, y

    return 0, 0

def subgrid_at_location(x, y, full_grid, width, height):
    sub_grid = []
    return sub_grid
