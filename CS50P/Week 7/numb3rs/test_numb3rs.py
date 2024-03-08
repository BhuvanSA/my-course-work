from numb3rs import validate


def test_validate_ip():
    assert validate("192.168.0.1") == True
    assert validate("1.1.1.1") == True
    assert validate("1.1.1.1.2") == False
    assert validate("255.256.1.0") == False
    assert validate("-1.0.-43.42") == False


def test_validate_str():
    assert validate("cat") == False
    assert validate("dog") == False
    assert validate("Jaime.lannister.the.son") == False
    assert validate("a.b.c.d") == False
