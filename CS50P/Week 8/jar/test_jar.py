from jar import Jar
import pytest


def test_init():
    jar1 = Jar()
    jar2 = Jar(10)
    assert jar1.capacity == 12
    assert jar2.capacity == 10


def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(10)
    assert jar.size == 10
    with pytest.raises(ValueError):
        assert jar.deposit(13)


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(4)
    assert jar.size == 1
    with pytest.raises(ValueError):
        assert jar.withdraw(2)
