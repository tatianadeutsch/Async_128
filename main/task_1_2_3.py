import multiprocessing
import time
import math
from multiprocessing import active_children, freeze_support

start_time = time.time()
def find_divisors_(n, start, end):

    divisors = []
    for i in range(start, end):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  # Добавляем парный делитель, если он не равен i
                divisors.append(n // i)
    return divisors


def parallel_divisors_(n):

    num_workers = multiprocessing.cpu_count()

    # Определяем диапазоны для каждого процесса
    step = math.isqrt(n) // num_workers + 1
    tasks = [(n, i, min(i + step, math.isqrt(n) + 1)) for i in range(1, math.isqrt(n) + 1, step)]

    # Используем пул процессов с контекстным менеджером
    with multiprocessing.Pool(num_workers) as pool:

        # Выполняем задачи параллельно
        results = pool.starmap_async(find_divisors_, tasks).get()

        # Узнаем от нечего делать, сколько дочерних процессов запущено в настоящий момент
        children = active_children()
        print(f'Количество активных процессов: {len(children)}')
        for child in children:
            print(child)




    # Объединяем и сортируем все найденные делители
    all_divisors = set()
    for sublist in results:
        all_divisors.update(sublist)
    # pool.join()

    return sorted(all_divisors)



number = 12345678
divisors = parallel_divisors_(number)
print(f"Делители числа {number}: {divisors}")

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Время выполнения задачи с 8 процессами: {elapsed_time:.4f} секунд")
# Узнаем, остались ли запущенные дочерние процессы
children = active_children()
print(f'Active Children Count: {len(children)}')


# if __name__ == '__main__':
#     freeze_support()

if __name__ == '__main__':
    parallel_divisors_(12345678)