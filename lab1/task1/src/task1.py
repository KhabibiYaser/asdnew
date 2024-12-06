# -*- coding: utf-8 -*-
from lab1.utils import *
import sys
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)


def insertion_sort(arr):
    """
    Реализация алгоритма сортировки вставкой.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def sort_main():
    """
    Главная функция для чтения массива из input.txt, сортировки и записи результата в output.txt.
    """
    _, arr = file_read_size_int_array()  # Читаем данные
    if not (1 <= len(arr) <= 10 ** 3):
        raise ValueError("Размер массива должен быть в пределах 1 <= n <= 10^3")
    if any(abs(x) > 10 ** 9 for x in arr):
        raise ValueError("Все элементы массива должны быть по модулю не больше 10^9")

    sorted_arr = insertion_sort(arr)  # Сортируем массив
    file_write(sorted_arr)  # Записываем результат в файл


if __name__ == '__main__':
    measure_performance(sort_main)

