# -*- coding: utf-8 -*-
from lab1.utils import *
import sys
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)


def swap_elements(arr, x, y, swaps):
    """
    Меняет элементы массива и записывает операцию в список swaps.
    """
    arr[x], arr[y] = arr[y], arr[x]
    swaps.append(f"Swap elements at indices {x + 1} and {y + 1}.")


def selection_sort_with_swaps(arr):
    """
    Реализация сортировки выбором с записью всех перестановок.
    """
    n = len(arr)
    swaps = []
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            swap_elements(arr, i, min_index, swaps)
    swaps.append("No more swaps needed.")
    return swaps


def sort_main():
    """
    Главная функция для чтения данных, сортировки и записи результата.
    """
    _, arr = file_read_size_int_array()  # Читаем данные
    if not (3 <= len(arr) <= 5000):
        raise ValueError("Размер массива должен быть в пределах 3 <= n <= 5000")
    if any(abs(x) > 10 ** 9 for x in arr):
        raise ValueError("Все элементы массива должны быть по модулю не больше 10^9")

    swaps = selection_sort_with_swaps(arr)  # Сортируем массив с записью перестановок
    file_write(swaps, line_by_line=True)  # Записываем перестановки в файл


if __name__ == '__main__':
    measure_performance(sort_main)
