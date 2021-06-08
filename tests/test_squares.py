from programs.list_of_squares import list_of_squares

def test_los_1():
    assert list_of_squares(1) =={1:1}

def test_los_4():
    assert list_of_squares(4) == {1:1,2:4,3:9,4:16}