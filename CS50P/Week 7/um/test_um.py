from um import count


def test_um_edge():
    assert count("um") == 1
    assert count("um I will take the chiron um") == 2


def test_upperCase():
    assert count("Um") == 1


def test_punc():
    assert count("um,") == 1
    assert count("Um, thanks, um...") == 2
    assert count("Um, thanks for the album.") == 1
