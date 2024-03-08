from fuel import convert, gauge
import pytest


def test_convert_accuracy():
    assert convert("5/10") == 50
    assert convert("1/4") == 25


def test_convert_valueError():
    with pytest.raises(ValueError):
        convert("10/5")


def test_convert_zeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("10/0")


def test_convert_valueNotAnInteger():
    with pytest.raises(ValueError):
        convert("5/ten")


def test_gauge_f():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"


def test_gauge_str():
    with pytest.raises(TypeError):
        gauge("50")
