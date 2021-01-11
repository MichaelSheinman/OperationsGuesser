from memory_solver import OperationGuess
import random


def test_one_number():
    """
    Verify that one number can form target
    """
    o = OperationGuess()
    for i in range(100):
        assert o.solve((i,), i) == str(i)


def test_addition():
    """
    Verify that the program can add correctly
    """
    o = OperationGuess()
    additionSol = o.solve((1, 2, 3, 4), 10)
    assert additionSol.count("+") == 3
    assert "1" in additionSol and "2" in additionSol
    assert "3" in additionSol and "4" in additionSol


def test_exceed():
    """Verify that the program cannot
    exceed the maximum generated value """
    numbers = tuple()
    product = 1
    for _ in range(5):
        rn = random.randint(2, 10)
        product *= rn
        numbers = numbers + (rn,)

    o = OperationGuess()
    assert o.solve(numbers, product + 1) == "Impossible"


def test_increase():
    """
    Given 50, 25, 2, i
    (50/25)/2 + i == i + 1
    """
    o = OperationGuess()
    for i in range(100):
        assert o.solve((50, 25, 2, i), i + 1) != 'Impossible'


def test_sum_difference():
    """
    Let j be a random number
    We want to verify that
    [j, j+1, j+2, 4, 6, 7]
    Can always be evaluated to:
    (j + j + 1 + j + 2) - (4 - 6 + 7)
    """
    o = OperationGuess()
    for j in range(1, 10):
        numbers = (4, 6, 7, j, j+1, j + 2)
        target = (j + j + 1 + j + 2) - (4 - 6 + 7)
        assert o.solve(numbers, target) != "Impossible"


def test_division():
    o = OperationGuess()
    val = o.solve((1000, 25, 2, 2), 21)
    assert val != "Impossible"


def test_nested():
    o = OperationGuess()
    val = o.solve((55, 2, 3, 1, 18), 360)
    assert val != "Impossible"


def test_failing():
    o = OperationGuess()
    product = 1
    numbers = (3, 3, 2, 10, 5)
    for number in numbers:
        product *= number
    assert o.solve(numbers, product + 1) == "Impossible"


def test_failing2():
    o = OperationGuess()
    numbers = (5, 5, 0)
    assert o.solve(numbers, 1000) == "Impossible"


def test_edge():
    """
    Check that we can detect
    (999 - 44 - 79 * 501) * 203
    """
    o = OperationGuess()
    numbers = (999, 44, 79, 501, 203)
    val = o.solve(numbers, -7840672)
    assert val != "Impossible"


def test_edge_two():
    """
    Check that we can detect
    ((99 + 11) / 11 + 1) * 888
    """
    o = OperationGuess()
    numbers = (99, 11, 11, 1, 888)
    val = o.solve(numbers, 9768)
    assert val != "Impossible"


if __name__ == '__main__':
    import pytest
    pytest.main(['tests.py'])
