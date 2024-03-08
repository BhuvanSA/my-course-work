import pytest
from project import get_joke, print_jokes, sayer
import asyncio


def test_get_joke_amount():
    assert len(asyncio.run(get_joke(2, "java"))) == 2


def test_get_joke_error():
    with pytest.raises(ValueError):
        assert asyncio.run(get_joke(11, "java"))


def test_sayer_output():
    assert sayer("hey david malan", "hey", 0) == None


def test_sayer_error():
    with pytest.raises(TypeError):
        assert sayer("hey david malan", "hey") == None


def test_print_jokes_output():
    assert print_jokes(['jaime', 'lnster']) == None


def test_print_jokes_error():
    with pytest.raises(TypeError):
        assert print_jokes(1)
