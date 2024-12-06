from lab0.utils import *
# -*- coding: utf-8 -*-

import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)

def calc_fib(n):
    """
    Эффективный алгоритм для вычисления числа Фибоначчи.
    Использует итеративный подход вместо рекурсии.
    """
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

def fibonacci_main():
    """
    Главная функция для чтения числа из input.txt, вычисления числа Фибоначчи и записи результата в output.txt.
    """
    _, arr = file_read_size_int_array()  # Читаем данные
    if len(arr) != 1:
        raise ValueError("Файл должен содержать ровно одно число.")
    n = arr[0]
    if not (0 <= n <= 45):
        raise ValueError("n должно быть в диапазоне 0 <= n <= 45")
    result = calc_fib(n)  # Вычисляем число Фибоначчи
    file_write([result])  # Записываем результат в файл

if __name__ == '__main__':
    measure_performance(fibonacci_main)
