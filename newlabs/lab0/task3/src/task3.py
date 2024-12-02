from lab0.utils import *
# -*- coding: utf-8 -*-

import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)

def last_digit_of_fib(n):

    if n < 0:
        raise ValueError("n должно быть неотрицательным")

    # Остаток от деления на 60 из-за периодичности
    n = n % 60

    # Вычисляем последнюю цифру с помощью итеративного подхода
    prev, curr = 0, 1
    for _ in range(n - 1):
        prev, curr = curr, (prev + curr) % 10
    return curr if n > 0 else 0


def last_digit_main():
    """
    Главная функция для чтения n из input.txt, вычисления последней цифры F_n и записи результата в output.txt.
    """
    _, arr = file_read_size_int_array()  # Читаем данные
    if len(arr) != 1:
        raise ValueError("Файл должен содержать ровно одно число.")
    n = arr[0]
    if not (0 <= n <= 10 ** 7):
        raise ValueError("n должно быть в диапазоне 0 <= n <= 10^7")
    result = last_digit_of_fib(n)  # Вычисляем последнюю цифру F_n
    file_write([result])  # Записываем результат в файл


if __name__ == '__main__':
    measure_performance(last_digit_main)
