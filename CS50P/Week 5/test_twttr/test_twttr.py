import pytest
from twttr import shorten


def test_allVowels():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("aEioU") == ""


def test_nonVowels():
    assert shorten(
        "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ") == "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"


def test_combination():
    assert shorten(
        "Jaime Lannister") == "Jm Lnnstr"


def test_int():
    with pytest.raises(TypeError):
        shorten(4)


def test_numbers():
    assert shorten('1234567890') == '1234567890'
    assert shorten('a1b2c3') == '1b2c3'


def test_punctuation():
    assert shorten('!*?#$@,') == '!*?#$@,'
    assert shorten('omg!') == 'mg!'
