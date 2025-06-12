import math
import numpy as np

original_dungeon_content = []
with open("./dungeons/dungeon01.txt", "r", encoding="UTF-8") as file:
    for l in file:
        trimmed_line = l.rstrip().lstrip()
        split_line = list(l.rstrip().lstrip())
        original_dungeon_content.append(split_line)

def blow_up_map(mini_map, size):
    if size % 2 == 0:
        raise ValueError(f"{size} must be odd")

    file_expansion = []
    for line in mini_map:
        line_expansion = []

        for char in line:
            if char in [" ", "#", "X"]:
                line_expansion.append(np.array(make_grid_for_space(size)))
            elif char == "-":
                line_expansion.append(np.array(make_grid_for_dash(size)))
            elif char == "|":
                line_expansion.append(np.array(make_grid_for_pipe(size)))
            if char == "*":
                line_expansion.append(np.array(make_grid_for_user(size)))

        file_expansion.append(line_expansion)

    ret_val = np.block(file_expansion)
    return ret_val

def make_grid_for_space(size):
    grid = []
    for _ in range(0, size):
        row = []

        for _ in range(0, size):
            row.append(" ")

        grid.append(row)
    return grid

def make_grid_for_user(size):
    grid = []
    for i in range(0, size):
        row = []

        for j in range(0, size):
            if i == int(size / 2) and j == int(size / 2):
                character = "*"
            else:
                character = " "
            row.append(character)

        grid.append(row)
    return grid

def make_grid_for_dash(size):
    grid = []
    for index in range(0, size):
        row = []

        character = "-" if index == int(size / 2) else " "

        for _ in range(0, size):
            row.append(character)

        grid.append(row)
    return grid

def make_grid_for_pipe(size):
    grid = []
    for _ in range(0, size):
        row = []

        for index in range(0, size):
            character = "|" if index == int(size / 2) else " "

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
    starting_x = x - math.floor(width / 2)
    starting_y = y - math.floor(height / 2)
    ending_x = starting_x + width
    ending_y = starting_y + height

    sub_grid = []
    for i in range(starting_y, ending_y):
        row = []
        for j in range(starting_x, ending_x):
            character = fetch_char_in_grid(full_grid, i, j)
            row.append(character)
        sub_grid.append(row)

    return sub_grid

def fetch_char_in_grid(full_grid, i, j):
    try:
        return full_grid[i][j]
    except IndexError:
        return ' '

def render_map(a):
    return "\n".join("".join(row) for row in a)
