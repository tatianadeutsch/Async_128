"""Реализуйте асинхронный метод, который будет
отправлять запросы в http://google.com по http
с ограничением не более 10 запросов в единицу времени."""

import asyncio
import aiohttp
from aiohttp import ClientSession
import time


start_time = time.time()
# Ограничение на количество одновременных запросов
MAX_REQUESTS_PER_SECOND = 10


async def fetch(session: ClientSession, url: str) -> None:
    """Отправляет GET-запрос и выводит статус."""
    async with session.get(url) as response:
        print(f"Status: {response.status}")


async def bound_fetch(sem: asyncio.Semaphore, session: ClientSession, url: str) -> None:
    """Заворачивает fetch в семафор для ограничения скорости."""
    async with sem:
        await fetch(session, url)


async def run_requests(n: int, url: str) -> None:
    """Запускает n запросов с ограничением на скорость."""
    # Создаем семафор для ограничения скорости запросов
    sem = asyncio.Semaphore(MAX_REQUESTS_PER_SECOND)

    async with aiohttp.ClientSession() as session:
        tasks = []

        for _ in range(n):
            # Запускаем задачу с использованием семафора
            task = asyncio.create_task(bound_fetch(sem, session, url))
            tasks.append(task)

            # Ожидаем окончания 1 секунды перед отправкой следующей порции запросов
            if len(tasks) % MAX_REQUESTS_PER_SECOND == 0:
                await asyncio.sleep(1)

        # Ожидаем завершения всех задач
        await asyncio.gather(*tasks)


async def main():
    url = "http://google.com"
    number_of_requests = 25  # Количество запросов, которые нужно отправить


    await run_requests(number_of_requests, url)



# Запуск основной функции
if __name__ == "__main__":
    asyncio.run(main())
end_time = time.time()

print(f"All requests completed in {end_time - start_time:.2f} seconds.")


import asyncio
from asyncio import Semaphore
import aiohttp

start_time = time.time()

url = 'http://google.com'
semaphore = Semaphore(10)  # Ограничение на 10 запросов одновременно


async def fetch(url, sem):
    async with sem:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()


async def main(n):
    await asyncio.gather(*[fetch(url, semaphore) for _ in range(1, n + 1)])


if __name__ == '__main__':
    asyncio.run(main(10))

end_time = time.time()

print(f"All requests completed in {end_time - start_time:.2f} seconds.")





