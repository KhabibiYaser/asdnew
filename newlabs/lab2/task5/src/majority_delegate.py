# -*- coding: utf-8 -*-

from lab2.utils import *
from lab2.task1.src.merge_sort import *
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)

def majority_delegate(array):
    n = len(array)
    if n == 0:
        return 0

    candidate = array[n // 2] # выбираем центральный элемент потому что массив отсортриован
    count = 0

    for i in range(n):
        if array[i] == candidate:
            count += 1

    if count > n // 2:
        return 1
    return 0


def majority_delegate_main():
    n, arr = file_read_size_int_array()
    sorted_arr = merge_sort(arr) # получается отсортированный массив
    file_write([majority_delegate(sorted_arr)])


if __name__ == "__main__":
    majority_delegate_main()