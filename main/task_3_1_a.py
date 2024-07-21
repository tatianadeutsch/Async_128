"""Реализуйте асинхронный метод, который будет
отправлять запросы в http://google.com по http
с ограничением не более 10 запросов в единицу времени."""

import asyncio
from asyncio import Semaphore

from aiohttp import ClientSession
import time

start_time = time.time()
# Ограничитель на 10 запросов
max_request_sec = 10
semaphore = Semaphore(max_request_sec)
url = 'http://google.com'



async def fetch(session: ClientSession, url: url) -> int:
    """Отправляет GET-запрос"""
    async with session.get(url) as response:
        print(f"Status: {response.status}")
        return response.status

async def fetch_with_semaphore(semaphore, session: ClientSession, url: url) -> int:
    """Использут семафор для GET-запросов"""
    async with semaphore:
        return await fetch(session, url)

async def run_requests(n: int, url: url) ->  list[int]:
    """Запускает запросы в количестве n с ограничением скорости"""
    async with ClientSession() as session:
        tasks = []
        for _ in range(n):
            # Запускаем задачу с использованием семафора
            task = asyncio.create_task(fetch_with_semaphore(semaphore, session, url))
            tasks.append(task)

            # Ожидаем окончания 1 секунды перед отправкой следующей порции запросов
            if len(tasks) % max_request_sec == 0:
                await asyncio.sleep(1)

         # Ожидаем завершения всех задач
        results = await asyncio.gather(*tasks)
    return results

async def main():
    number_of_requests = 30  # Количество запросов, которые нужно отправить


    await run_requests(number_of_requests, url)

if __name__ == "__main__":
    asyncio.run(main())


end_time = time.time()

print(f"All requests completed in {end_time - start_time:.2f} seconds.")

# Максимальное количество запросов = 30, дальше ошибка 429