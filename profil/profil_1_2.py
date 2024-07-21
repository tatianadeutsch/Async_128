import cProfile
import pstats
import io
from multiprocessing import Process, active_children

from main.task_1_2 import task, processing_task


def profile_task():
    # Создаем строковый поток для записи профилировочной информации
    pr = cProfile.Profile()
    with pr:
        # pr.enable()  # Начинаем профилирование
        task(12345678)  # Выполняем целевую функцию
        # pr.disable()  # Завершаем профилирование

    # Выводим результаты профилирования
    s = io.StringIO()
    # Сортирует результаты по совокупному времени, которое показывает, сколько времени затрачивается на выполнение функций.
    sortby = 'cumulative'
    # Используется для создания объекта Stats, который может анализировать и форматировать профилировочные данные
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    # Выводит результаты профилирования.
    ps.print_stats()
    print(s.getvalue())

if __name__ == '__main__':
    print("Profiling task function:")
    profile_task()
    print("\nRunning processing_task:")
    processing_task(12345678)