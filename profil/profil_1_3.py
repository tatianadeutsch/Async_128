import time
import cProfile
import multiprocessing
import pstats
import io
from multiprocessing import active_children, freeze_support

from main.task_1_2_3 import parallel_divisors_


def profile_parallel_divisors(n):
    # Создаем строковый поток для записи профилировочной информации
    pr = cProfile.Profile()
    pr.enable()  # Начинаем профилирование
    divisors = parallel_divisors_(n)
    pr.disable()  # Завершаем профилирование

    # Выводим результаты профилирования
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
    return divisors

if __name__ == '__main__':

    number = 12345678
    print("Profiling parallel_divisors_ function:")
    divisors = profile_parallel_divisors(number)

    print(f"Делители числа {number}: {divisors}")

