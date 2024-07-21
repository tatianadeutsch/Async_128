import asyncio
from asyncio import Semaphore
import aiohttp
import yappi

from main.task_3_1_a import run_requests, url


async def main():
    number_of_requests = 30  # Количество запросов, которые нужно отправить
    await run_requests(number_of_requests, url)

if __name__ == "__main__":
    # Запускаем профилирование
    yappi.start()

    # Выполняем асинхронный код
    asyncio.run(main())

    # Останавливаем профилирование
    yappi.stop()

    # Получаем и выводим результаты
    yappi.get_func_stats().print_all()
    yappi.get_thread_stats().print_all()
