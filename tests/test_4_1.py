import pytest
import aiohttp
import asyncio
from asyncio import Semaphore
from unittest.mock import patch, AsyncMock

# Импортируем тестируемые функции
from main.task_4_1 import fetch, fetch_with_semaphore, run_requests
@pytest.mark.asyncio
async def test_fetch():
    """Тестируем функцию fetch."""
    url = "https://httpbin.org/status/200"  # Используем тестовый URL
    async with aiohttp.ClientSession() as session:
        status = await fetch(session, url)
        assert status == 200  # Проверяем, что статус успешный

@pytest.mark.asyncio
async def test_fetch_with_semaphore():
    """Проверяет, что функция fetch_with_semaphore корректно
    работает с семафором и возвращает статус 200."""
    url = "https://httpbin.org/status/200"
    semaphore = Semaphore(5)
    async with aiohttp.ClientSession() as session:
        status = await fetch_with_semaphore(semaphore, session, url)
        assert status == 200

@pytest.mark.asyncio
async def test_run_requests():
    """Тестируем функцию run_requests на корректное количество запросов и статусов."""
    url = "https://httpbin.org/status/200"
    num_requests = 50
    max_requests = 10

    # Использует unittest.mock.patch для имитации функции fetch,
    # чтобы она всегда возвращала статус 200.
    with patch('main.task_4_1.fetch', new_callable=AsyncMock) as mock_fetch:
        mock_fetch.return_value = 200  # Все запросы возвращают статус 200

        results = await run_requests(url, num_requests, max_requests)

        # Проверяем, что функция вернула правильное количество статусов
        assert len(results) == num_requests
        assert all(status == 200 for status in results)  # Все статусы должны быть 200

        # Проверяем запись в файл
        with open("response_statuses.txt", 'r') as f:
            lines = f.readlines()
            assert len(lines) == num_requests
            assert all("Status 200" in line for line in lines)

if __name__ == "__main__":
    pytest.main()