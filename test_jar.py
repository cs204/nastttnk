from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar._capacity == 12


def test_deposit():
    jar = Jar(5)
    jar.deposit(4)
    assert jar.size == 4
    with pytest.raises(ValueError):
        jar.deposit(2)

def test_str():
    jar = Jar()
    jar.deposit(3)
    assert jar.__str__() == 3 * "🍪"

def test_withdraw():
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(3)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(2)


def test_size():
    jar = Jar()
    jar._capacity = 12
    jar._size = 10
    assert jar.size == 10
    jar.size = 11
    with pytest.raises(ValueError):
        jar.size = 13
    with pytest.raises(ValueError):
        jar.size = -3
    with pytest.raises(ValueError):
        jar.size = 3.5

def test_capacity():
    jar = Jar()
    jar.capacity = 12
    assert jar.capacity == 12
    jar.capacity = 13
    with pytest.raises(ValueError):
        jar.capacity = -3
    with pytest.raises(ValueError):
            jar.capacity = 3.5






