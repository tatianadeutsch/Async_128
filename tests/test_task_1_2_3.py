import pytest
from unittest.mock import patch, MagicMock

from main.task_1_2_3 import find_divisors_, parallel_divisors_


def test_find_divisors_():
    # Проверяем нахождение делителей для числа 28 в диапазоне от 1 до 6
    n = 28
    start, end = 1, 6
    expected_divisors = [1, 28, 2, 14, 4, 7]
    assert sorted(find_divisors_(n, start, end)) == sorted(expected_divisors)

    # Проверяем нахождение делителей в другом диапазоне
    start, end = 6, 15
    expected_divisors = [7, 4, 14, 2]
    assert sorted(find_divisors_(n, start, end)) == sorted(expected_divisors)

@patch('main.task_1_2_3.active_children')
@patch('main.task_1_2_3.multiprocessing.Pool')
def test_parallel_divisors_(mock_pool, mock_active_children):
    # Настройка мока для возвращения контролируемых значений
    mock_active_children.return_value = [MagicMock(), MagicMock()]

    # Предопределенный результат для моков
    mock_pool.return_value.__enter__.return_value.starmap.return_value = [
        [1, 28, 2, 14], [4, 7]
    ]

    n = 28
    expected_divisors = [1, 2, 4, 7, 14, 28]

    assert parallel_divisors_(n) == expected_divisors

    # Проверяем, что Pool и starmap вызваны корректно
    mock_pool.assert_called_once()
    mock_pool.return_value.__enter__.return_value.starmap.assert_called_once()

    # Проверяем, что active_children было вызвано для получения списка активных процессов
    mock_active_children.assert_called_once()

if __name__ == '__main__':
    pytest.main()