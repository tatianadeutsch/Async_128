import os

import pytest

from main.task_1 import get_divisors


def test_get_divisors_ok():
    assert get_divisors(12345678) == [1, 2, 3, 6, 9, 18, 47, 94, 141, 282, 423, 846, 14593, 29186, 43779, 87558, 131337,
                                      262674, 685871, 1371742, 2057613, 4115226, 6172839, 12345678]


def test_get_divisors_raises():
    with pytest.raises(ValueError) as error:
        get_divisors(10000)
    assert "Введите число от 1 000 000 до 2 000 000"


@pytest.mark.parametrize("test_input, expected_result", [(-10000, "Введите число от 1 000 000 до 2 000 000"),
                                                         (20000001, "Введите число от 1 000 000 до 2 000 000")])
def test_divisors_raises(test_input, expected_result):
    with pytest.raises(ValueError) as error:
        get_divisors(test_input)
    assert expected_result


if __name__ == '__main__':
    pytest.main()