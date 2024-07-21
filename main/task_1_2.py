import multiprocessing
import time
import math

from multiprocessing import Process, active_children, cpu_count

start_time = time.time()

def task(n):
    if n < 1000000 or n > 20000000:
        raise ValueError(f"Введите число от 1 000 000 до 20 000 000")
    divisors = []
    for i in range(1, int(n + 1)):
        if n % i == 0:
            divisors.append(i)
    print(sorted(divisors))
    return sorted(divisors)

def processing_task(number):
    process = Process(target=task, args=(number,))
    process.start()
    children = active_children()
    print(f'Количество активных процессов: {len(children)}')
    for child in children:
        print(child)
    process.join()


if __name__ == '__main__':
    processing_task(12345678)


end_time = time.time()
elapsed_time = end_time - start_time
print(f"Время выполнения задачи с 1 дочерним процессом: {elapsed_time:.4f} секунд")



