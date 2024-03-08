import pytest
from bank import value


def test_nonH():
    assert value("chomreabsuor") == 100
    assert value("zdraveite") == 100
    assert value("Ahoj") == 100


def test_oneH():
    assert value("Hej") == 20
    assert value("Hallo") == 20
    assert value("hailo") == 20


def test_hello():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("HELLO") == 0


def test_int():
    with pytest.raises(AttributeError):
        value(123)


def test_number():
    assert value("123456") == 100
    assert value("h12345") == 20
    assert value("hello 123") == 0
