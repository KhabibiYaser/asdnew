# -*- coding: utf-8 -*-
from lab2.utils import *
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target: # централный элемент больше или меньше
            return mid
        if arr[mid] < target:
            left = mid + 1   # если больше, то переходим к левой половине
        else:
            right = mid - 1 # ищем уже в правой половине
    return -1 # нет найдйен


def binary_search_main():
    with open('../txtf/input.txt', 'r') as file: # input был спецефический, поэтому тут свой
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().strip().split()))
        k = int(file.readline().strip())
        b = list(map(int, file.readline().strip().split()))

    results = []
    for target in b:
        index = binary_search(arr, target)
        results.append(index)

    file_write(results)
    return arr, b

if __name__ == '__main__':
    measure_performance(binary_search_main)
