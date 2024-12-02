# -*- coding: utf-8 -*-

from lab2.utils import *
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)

def kadane(array):
    if len(array) == 0:
        raise ValueError("Input array is empty.")

    max_so_far = max_ending_here = array[0]    # какой максимальный now init (1 элементов)
    start = end = start_new = 0

    for i in range(1, len(array)):
        if array[i] > max_ending_here + array[i]:
            max_ending_here = array[i]   # прервыаемся
            start_new = i               # начало нового подмассива
        else:
            max_ending_here += array[i]        # если оборвемся , то насколько это будет выгодно

        if max_ending_here > max_so_far:       # проверка оборваться или continue
            max_so_far = max_ending_here
            start = start_new                 # подсчет нового подмассива
            end = i

    return start, end, max_so_far # для использования в 6 задаче тк там нужнен стартовый и конечный индекс

def kadane_main():
    n, arr = file_read_size_int_array()
    start, end, max_subarray = kadane(arr)
    file_write([max_subarray])


if __name__ == '__main__':
    measure_performance(kadane_main)
