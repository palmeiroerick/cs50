import pytest

from jar import Jar


def test_capacity():
    assert Jar(8).capacity == 8
    assert Jar(4).capacity == 4
    with pytest.raises(ValueError):
        jar = Jar(-1)


def test_size():
    jar = Jar(10)
    assert jar.size == 0
    jar.size = 4
    assert jar.size == 4
    jar.size = 7
    assert jar.size == 7
    jar.size = 10
    assert jar.size == 10


def test_deposit():
    jar = Jar(10)
    jar.deposit(6)
    assert jar.size == 6
    jar.deposit(2)
    assert jar.size == 8
    with pytest.raises(ValueError):
        jar.deposit(4)


def test_withdraw():
    jar = Jar(10)
    jar.deposit(10)
    jar.withdraw(6)
    assert jar.size == 4
    with pytest.raises(ValueError):
        jar.withdraw(5)
