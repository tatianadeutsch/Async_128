import threading
import time

start_time = time.time()
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


end_time = time.time()
elapsed_time = end_time - start_time
print(f"Время выполнения задачи: {elapsed_time:.4f} секунд")