import pytest

from game.dungeon_helper import original_dungeon_content, blow_up_map

def test_original_dungeon_map_has_right_size():
    assert len(original_dungeon_content) == 10
    for line in original_dungeon_content:
        assert len(line) == 35

@pytest.mark.skip("will come back to this later")
def test_blown_up_dungeon_with_empty_map_sections():
    mini_map = ([" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "])
    big_map = blow_up_map(mini_map)

    assert len(big_map) == 300
    expected_line = "".join([" " for x in range(0, 300)])
    for line in big_map:
        assert line == expected_line

@pytest.mark.skip("will come back to this later")
def test_blown_up_dungeon_is_bigger():
    mini_map = ([" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "])
    big_map = blow_up_map(mini_map)

    assert len(big_map) == 300
    expected_line = "".join([" " for x in range(0, 300)])
    for line in big_map:
        assert line == expected_line

def test_single_empty_cell():
    s = [[" "]]

    big_map = blow_up_map(s, 3)
    rendered_big_map = doit(big_map)

    expected_big_map = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]
    rendered_expected_big_map = doit(expected_big_map)

    assert rendered_big_map == rendered_expected_big_map

def test_single_horizontal_wall():
    s = [["-"]]

    big_map = blow_up_map(s, 3)
    rendered_big_map = doit(big_map)

    expected_big_map = [
            [" ", " ", " "],
            ["-", "-", "-"],
            [" ", " ", " "]]
    rendered_expected_big_map = doit(expected_big_map)

    assert rendered_big_map == rendered_expected_big_map

def test_single_vertical_wall():
    s = [["|"]]

    big_map = blow_up_map(s, 3)
    rendered_big_map = doit(big_map)

    expected_big_map = [
            [" ", "|", " "],
            [" ", "|", " "],
            [" ", "|", " "]]
    rendered_expected_big_map = doit(expected_big_map)

    assert rendered_big_map == rendered_expected_big_map

def test_three_by_three_grid():
    s = [[" ", " ", "|"],
         [" ", "-", " "],
         ["|", " ", "-"]]

    big_map = blow_up_map(s, 3)
    rendered_big_map = doit(big_map)

    expected_big_map = [[" ", " ", " ",   " ", " ", " ",   " ", "|", " "],
                        [" ", " ", " ",   " ", " ", " ",   " ", "|", " "],
                        [" ", " ", " ",   " ", " ", " ",   " ", "|", " "],

                        [" ", " ", " ",   " ", " ", " ",   " ", " ", " "],
                        [" ", " ", " ",   "-", "-", "-",   " ", " ", " "],
                        [" ", " ", " ",   " ", " ", " ",   " ", " ", " "],

                        [" ", "|", " ",   " ", " ", " ",   " ", " ", " "],
                        [" ", "|", " ",   " ", " ", " ",   "-", "-", "-"],
                        [" ", "|", " ",   " ", " ", " ",   " ", " ", " "]]
    rendered_expected_big_map = doit(expected_big_map)

    assert rendered_big_map == rendered_expected_big_map

def test_scale_by_one():
    s = [[" "]]

    big_map = blow_up_map(s, 1)
    rendered_big_map = doit(big_map)

    expected_big_map = [[" "]]
    rendered_expected_big_map = doit(expected_big_map)

    assert rendered_big_map == rendered_expected_big_map

def doit(a):
    return "".join("".join(row) for row in a)
