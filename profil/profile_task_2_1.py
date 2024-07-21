import threading
import cProfile
import pstats
import io


def create_file(index):
    """
    Принимает индекс, создаёт файл с соответствующим именем и записывает индекс внутрь файла.
    :param index: номер файла
    :return: созданные файлы
    """
    filename = f"file_{index}.txt"
    with open(filename, 'w') as file:
        file.write(str(index))
    print(f"Файл {filename} успешно создан.")
    return filename


def create_files_in_threads():
    threads = []

    # создаётся пул потоков с 10 рабочими потоками
    for i in range(10):
        thread = threading.Thread(target=create_file, args=(i,))
        threads.append(thread)
        thread.start()

    # ожидание завершения всех заданий и вывод информации о созданных файлах
    for thread in threads:
        thread.join()


def profile_func(func, *args):
    """Профилирует указанную функцию"""
    # Создаём профиль
    pr = cProfile.Profile()
    pr.enable()

    # Выполняем функцию
    func(*args)

    pr.disable()
    # Выводим статистику
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())


if __name__ == "__main__":
    # Профилирование функции создания файлов в потоках
    profile_func(create_files_in_threads)
