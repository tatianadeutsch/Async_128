import os

import pytest

from main.task_1_2 import task, processing_task



def test_get_divisors_ok():
    assert task(12345678) == [1, 2, 3, 6, 9, 18, 47, 94, 141, 282, 423, 846, 14593, 29186, 43779, 87558, 131337,
                                      262674, 685871, 1371742, 2057613, 4115226, 6172839, 12345678]


def test_get_divisors_raises():
    with pytest.raises(ValueError) as error:
        task(10000)
    assert "Введите число от 1 000 000 до 2 000 000"


@pytest.mark.parametrize("test_input, expected_result", [(-10000, "Введите число от 1 000 000 до 2 000 000"),
                                                         (20000001, "Введите число от 1 000 000 до 2 000 000")])
def test_divisors_raises(test_input, expected_result):
    with pytest.raises(ValueError) as error:
        task(test_input)
    assert expected_result


import pytest
from unittest.mock import patch, MagicMock



@patch('main.task_1_2.Process')
def test_processing_task(mock_process):
    # Мокаем процесс и его методы
    mock_instance = MagicMock()
    mock_process.return_value = mock_instance

    # Вызываем функцию
    processing_task(1_000_000)

    # Проверяем, что процесс был создан и запущен
    mock_process.assert_called_once_with(target=task, args=(1_000_000,))
    mock_instance.start.assert_called_once()
    mock_instance.join.assert_called_once()



if __name__ == '__main__':
    pytest.main()