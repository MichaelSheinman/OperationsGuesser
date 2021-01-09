import pytest
from solver import solve2


def test_one_number():
    """
    Verify that one number can form target
    """
    for i in range(100):
        assert solve2([i], i) == str(i)


def test_addition():
    """
    Verify that the program can add correctly
    """
    additionSol = solve2([1, 2, 3, 4], 10)
    assert additionSol.count("+") == 3
    assert "1" in additionSol and "2" in additionSol
    assert "3" in additionSol and "4" in additionSol


def test_increase():
    """
    Given 50, 25, 2, i
    (50/25)/2 + i == i + 1
    """
    for i in range(100):
        assert solve2([50, 25, 2, i], i + 1) != 'Impossible'


if __name__ == '__main__':
    import pytest
    pytest.main(['tests.py'])
