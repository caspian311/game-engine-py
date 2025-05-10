from game.dungeon_helper import dungeon_map, player_position_in_dungeon, player_surroundings

def test_dungeon_map_has_right_size():
    assert len(dungeon_map()) == 10
    for x in range(0, len(dungeon_map())):
        assert len(dungeon_map()[x]) == 35

def test_player_position():
    (x, y) = player_position_in_dungeon()

    assert x == 17
    assert y == 9

def test_player_position_gives_5_columns_and_5_rows_on_either_side():
    surroundings = player_surroundings()

    assert len(surroundings) == 6
    assert len(surroundings[0]) == 11
    assert "".join(surroundings[0]) == "-|     |---"
    assert "".join(surroundings[1]) == " |  X  |   "
    assert "".join(surroundings[2]) == " |-----|   "
    assert "".join(surroundings[3]) == "           "
    assert "".join(surroundings[4]) == "---|   |---"
    assert "".join(surroundings[5]) == "   | * |   "
