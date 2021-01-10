from solver import solve
import random


def test_one_number():
    """
    Verify that one number can form target
    """
    for i in range(100):
        assert solve([i], i) == str(i)


def test_addition():
    """
    Verify that the program can add correctly
    """
    additionSol = solve([1, 2, 3, 4], 10)
    assert additionSol.count("+") == 3
    assert "1" in additionSol and "2" in additionSol
    assert "3" in additionSol and "4" in additionSol


def test_exceed():
    """Verify that the program cannot
    exceed the maximum generated value """
    numbers = []
    product = 1
    for _ in range(5):
        rn = random.randint(2, 10)
        product *= rn
        numbers.append(rn)

    assert solve(numbers, product + 1) == "Impossible"


def test_increase():
    """
    Given 50, 25, 2, i
    (50/25)/2 + i == i + 1
    """
    for i in range(100):
        assert solve([50, 25, 2, i], i + 1) != 'Impossible'


def test_sum_difference():
    """
    Let j be a random number
    We want to verify that
    [j, j+1, j+2, 4, 6, 7]
    Can always be evaluated to:
    (j + j + 1 + j + 2) - (4 - 6 + 7)
    """
    for j in range(1, 10):
        numbers = [4, 6, 7]
        numbers.extend([j, j+1, j + 2])
        target = (j + j + 1 + j + 2) - (4 - 6 + 7)
        assert solve(numbers, target) != "Impossible"


def test_division():
    val = solve([1000, 25, 2, 2], 21)
    assert val != "Impossible"


def test_nested():
    val = solve([55, 2, 3, 1, 18], 360)
    print(val)
    assert val != "Impossible"


def test_failing():
    product = 1
    numbers = [3, 3, 2, 10, 5]
    for number in numbers:
        product *= number
    assert solve(numbers, product + 1) == "Impossible"


def test_failing2():
    numbers = [5, 5, 0]
    assert solve(numbers, 1000) == "Impossible"


def test_edge():
    """
    Check that we can detect
    (999 - 44 - 79 * 501) * 203
    """
    numbers = [999, 44, 79, 501, 203]
    val = solve(numbers, -7840672)
    assert val != "Impossible"


def test_edge_two():
    """
    Check that we can detect
    ((99 + 11) / 11 + 1) * 888
    """
    numbers = [99, 11, 11, 1, 888]
    val = solve(numbers, 9768)
    assert val != "Impossible"


if __name__ == '__main__':
    import pytest
    pytest.main(['tests.py'])
