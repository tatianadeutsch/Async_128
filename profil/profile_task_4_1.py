import asyncio
from asyncio import Semaphore
import aiohttp
from aiohttp import ClientSession
import time
import cProfile
import pstats
import io

from main.task_4_1 import main


def profile_async_func(func, *args):
    """Профилирует асинхронную функцию"""
    # Создаем профиль
    pr = cProfile.Profile()
    pr.enable()

    # Запускаем событие цикла
    asyncio.run(func(*args))

    pr.disable()
    # Выводим статистику
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())


if __name__ == "__main__":
    # Профилирование основного асинхронного кода
    profile_async_func(main)


