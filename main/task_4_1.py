"""Написать асинхронный код, который делает 50 get запросов к https://example.com/ .
Записать все статусы ответов в файл и убедиться, что количество запросов
соответствует заданному количеству.
Необходимо учесть, чтобы одновременно выполнялось не больше 10 запросов.
Для выполнения запросов использовать библиотеку aiohttp.
Все значения, количество запросов, лимит одновременно выполняемых запросов
и url должны передаваться как параметры."""


import asyncio
from asyncio import Semaphore

import aiohttp
from aiohttp import ClientSession
import time

start_time = time.time()

async def fetch(session: ClientSession, url) -> int:
    """Отправляет GET-запрос"""
    async with session.get(url) as response:
        print(f"Status: {response.status}")
        return response.status


async def fetch_with_semaphore(semaphore, session: ClientSession, url):
    """Использут семафор для GET-запросов"""
    async with semaphore:
        return await fetch(session, url)

async def run_requests(url, num_requests, max_requests):
    """Запускает запросы к указанному URL с заданными параметрами."""
    semaphore = Semaphore(max_requests)

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_with_semaphore(semaphore, session, url) for _ in range(num_requests)]

        # Ожидаем завершения всех задач
        results = await asyncio.gather(*tasks)
        with open("response_statuses.txt", 'w') as f:
            for i, status in enumerate(results, start=1):
                f.write(f"Request {i}: Status {status}\n")


        assert len(results) == num_requests
    print(f"Completed {len(results)} requests")
    return results


async def main():
    await run_requests("https://example.com/",50, 10)



if __name__ == "__main__":
    asyncio.run(main())


end_time = time.time()

print(f"All requests completed in {end_time - start_time:.2f} seconds.")

