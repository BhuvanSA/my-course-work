from working import convert
import pytest


def test_short():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_long():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_nightShift():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


def test_12AM():
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"


def test_value_error():
    with pytest.raises(ValueError):
        assert convert("13:61 PM to 12:00 AM")


def test_value_error2():
    with pytest.raises(ValueError):
        assert convert("10:30 PM - 8:50 AM")
