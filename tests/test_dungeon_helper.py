from game.dungeon_helper import original_dungeon_content, blow_up_map

def test_original_dungeon_map_has_right_size():
    assert len(original_dungeon_content) == 10
    for line in original_dungeon_content:
        assert len(line) == 35

def test_single_empty_cell():
    s = [[" "]]

    big_map = blow_up_map(s, 3)
    rendered_big_map = render_map(big_map)

    expected_big_map = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]
    rendered_expected_big_map = render_map(expected_big_map)

    assert rendered_big_map == rendered_expected_big_map

def test_single_horizontal_wall():
    s = [["-"]]

    big_map = blow_up_map(s, 3)
    rendered_big_map = render_map(big_map)

    expected_big_map = [
            [" ", " ", " "],
            ["-", "-", "-"],
            [" ", " ", " "]]
    rendered_expected_big_map = render_map(expected_big_map)

    assert rendered_big_map == rendered_expected_big_map

def test_single_vertical_wall():
    s = [["|"]]

    big_map = blow_up_map(s, 3)
    rendered_big_map = render_map(big_map)

    expected_big_map = [
            [" ", "|", " "],
            [" ", "|", " "],
            [" ", "|", " "]]
    rendered_expected_big_map = render_map(expected_big_map)

    assert rendered_big_map == rendered_expected_big_map

def test_three_by_three_grid():
    s = [[" ", " ", "|"],
         [" ", "-", " "],
         ["|", " ", "-"]]

    big_map = blow_up_map(s, 3)
    rendered_big_map = render_map(big_map)

    expected_big_map = [[" ", " ", " ",   " ", " ", " ",   " ", "|", " "],
                        [" ", " ", " ",   " ", " ", " ",   " ", "|", " "],
                        [" ", " ", " ",   " ", " ", " ",   " ", "|", " "],

                        [" ", " ", " ",   " ", " ", " ",   " ", " ", " "],
                        [" ", " ", " ",   "-", "-", "-",   " ", " ", " "],
                        [" ", " ", " ",   " ", " ", " ",   " ", " ", " "],

                        [" ", "|", " ",   " ", " ", " ",   " ", " ", " "],
                        [" ", "|", " ",   " ", " ", " ",   "-", "-", "-"],
                        [" ", "|", " ",   " ", " ", " ",   " ", " ", " "]]
    rendered_expected_big_map = render_map(expected_big_map)

    assert rendered_big_map == rendered_expected_big_map

def test_scale_single_cell_by_one():
    s = [[" "]]

    big_map = blow_up_map(s, 1)
    rendered_big_map = render_map(big_map)

    expected_big_map = [[" "]]
    rendered_expected_big_map = render_map(expected_big_map)

    assert rendered_big_map == rendered_expected_big_map

def test_scale_single_cell_by_five():
    s = [["-"]]

    big_map = blow_up_map(s, 5)
    rendered_big_map = render_map(big_map)

    expected_big_map = [[" ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " "],
                        ["-", "-", "-", "-", "-"],
                        [" ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " "]]
    rendered_expected_big_map = render_map(expected_big_map)

    assert rendered_big_map == rendered_expected_big_map

# pylint: disable=line-too-long
def test_big_test():
    s = [["-", "-", "|"],
         [" ", " ", "|"],
         ["-", " ", "|"]]

    big_map = blow_up_map(s, 7)
    rendered_big_map = render_map(big_map)

    expected_big_map = [[" ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", "|", " ", " ", " "],
                        [" ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", "|", " ", " ", " "],
                        [" ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", "|", " ", " ", " "],
                        ["-", "-", "-", "-", "-", "-", "-",  "-", "-", "-", "-", "-", "-", "-",  " ", " ", " ", "|", " ", " ", " "],
                        [" ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", "|", " ", " ", " "],
                        [" ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", "|", " ", " ", " "],
                        [" ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", "|", " ", " ", " "],

                        [" ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", "|", " ", " ", " "],
                        [" ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", "|", " ", " ", " "],
                        [" ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", "|", " ", " ", " "],
                        [" ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", "|", " ", " ", " "],
                        [" ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", "|", " ", " ", " "],
                        [" ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", "|", " ", " ", " "],
                        [" ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", "|", " ", " ", " "],

                        [" ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", "|", " ", " ", " "],
                        [" ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", "|", " ", " ", " "],
                        [" ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", "|", " ", " ", " "],
                        ["-", "-", "-", "-", "-", "-", "-",  " ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", "|", " ", " ", " "],
                        [" ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", "|", " ", " ", " "],
                        [" ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", "|", " ", " ", " "],
                        [" ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", " ", " ", " ", " ",  " ", " ", " ", "|", " ", " ", " "]]
    rendered_expected_big_map = render_map(expected_big_map)

    assert rendered_big_map == rendered_expected_big_map

def test_dont_scale_by_even_numbers():
    s = [[" "]]

    try:
        blow_up_map(s, 4)
        assert False
    except ValueError:
        assert True

def test_allow_scale_by_odd_numbers():
    s = [[" "]]

    try:
        blow_up_map(s, 1)
        blow_up_map(s, 3)
        blow_up_map(s, 5)
        blow_up_map(s, 7)
        blow_up_map(s, 9)
        blow_up_map(s, 11)

        assert True
    except ValueError:
        assert False

def render_map(a):
    return "\n".join("".join(row) for row in a)
