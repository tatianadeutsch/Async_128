import cProfile
import threading

from main.task_1 import get_divisors


def main_get_divisors():
    number = 12345678  # Замените на число в диапазоне от 1_000_000 до 20_000_000
    divisors = get_divisors(number)
    print(f"Делители числа {number}: {divisors}")




if __name__ == "__main__":
    cProfile.run('main_get_divisors()',)
