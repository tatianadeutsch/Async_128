
def get_divisors(n):
    """
    Дано число в диапазоне от 1_000_000 до 20_000_000.
    Получите список целочисленных делителей этого числа.
    :param n: целое число от 1 000 000 до 20 000 000
    :return: список целочисленных делителей n
    """
    if n < 1000000 or n > 20000000:
        raise ValueError(f"Введите число от 1 000 000 до 20 000 000")
    divisors = []
    for i in range(1, int(n + 1)):
        if n % i == 0:
            divisors.append(i)
    return sorted(divisors)


# Пример использования
number = 19999990
divisors = get_divisors(number)
print(f"Делители числа {number}: {divisors}")



"""
    Напишите скрипт который создаст параллельно 10
    файлов с именем `file_ {index}.txt' и записывает их номер внутрь файла."""

import threading


def create_file(index):
    """
    принимает индекс, создаёт файл с соответствующим именем и записывает индекс внутрь файла
    :param index: номер файла
    :return: созданные файлы
    """
    filename = f"file_{index}.txt"
    with open(filename, 'w') as file:
        file.write(str(index))
    print(f"Файл {filename} успешно создан.")
    return filename

threads = []

# создаётся пул потоков с 10 рабочими потоками
for i in range(10):
    thread = threading.Thread(target=create_file, args=(i,))
    threads.append(thread)
    thread.start()
# ожидание завершения всех заданий и вывод информации о созданных файлах
for thread in threads:
    thread.join()


