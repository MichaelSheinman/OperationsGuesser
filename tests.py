import pytest
from solver import solve2


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
