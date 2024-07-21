'''    Дано число в диапазоне от 1_000_000 до 20_000_000.
        Получите список целочисленных делителей этого числа.'''

import time

start_time = time.time()
def get_divisors(n):

    if n < 1000000 or n > 20000000:
        raise ValueError(f"Введите число от 1 000 000 до 20 000 000")
    divisors = []
    for i in range(1, int(n + 1)):
        if n % i == 0:
            divisors.append(i)
    return sorted(divisors)

if __name__ == '__main__':
    number = 12345678
    divisors = get_divisors(number)
    print(f"Делители числа {number}: {divisors}")

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Время выполнения задачи в синхронном режиме: {elapsed_time:.4f} секунд")




