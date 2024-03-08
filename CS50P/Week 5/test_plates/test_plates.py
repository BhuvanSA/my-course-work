from plates import is_valid
import pytest


def test_firstTwoLetters():
    assert is_valid("CS50") == True
    assert is_valid("0012") == False
    assert is_valid("C550") == False


def test_minMaxLength():
    assert is_valid("QW50") == True
    assert is_valid("QW5000000") == False
    assert is_valid("Q") == False


def test_middleNumbers():
    assert is_valid("AAA222") == True
    assert is_valid("AA222A") == False


def test_nonzeroFirstNumber():
    assert is_valid("AAA2") == True
    assert is_valid("AAA02") == False


def test_noPunctuationMarks():
    assert is_valid("AAA!22") == False
    assert is_valid("AA,933") == False


def test_int():
    with pytest.raises(TypeError):
        assert is_valid(933)
