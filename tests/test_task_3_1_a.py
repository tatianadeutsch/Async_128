import pytest
import asyncio
from aiohttp import ClientSession
from main.task_3_1_a import fetch, fetch_with_semaphore, run_requests, max_request_sec, url


@pytest.mark.asyncio
async def test_fetch():
    async with ClientSession() as session:
        status = await fetch(session, url)
        assert status == 200, "Статус должен быть 200"


@pytest.mark.asyncio
async def test_fetch_with_semaphore():
    semaphore = asyncio.Semaphore(max_request_sec)
    async with ClientSession() as session:
        status = await fetch_with_semaphore(semaphore, session, url)
        assert status == 200, "Статус должен быть 200"


@pytest.mark.asyncio
async def test_run_requests():
    number_of_requests = 30
    results = await run_requests(number_of_requests, url)
    assert len(results) == number_of_requests, "Кол-во результатов должно соответствовать кол-ву запросов"
    assert all(status == 200 for status in results), "Все запросы должны быть со статусом 200"


if __name__ == "__main__":
    pytest.main()
