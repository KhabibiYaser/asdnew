import random

from lab3.utils import *

import os , sys
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)


def partition(array, left, right):
    pivot_value = array[left]
    left_pointer = left
    for current_pointer in range(left + 1, right):
        if array[current_pointer] < pivot_value:
            left_pointer += 1
            array[left_pointer], array[current_pointer] = array[current_pointer], array[left_pointer]
    array[left], array[left_pointer] = array[left_pointer], array[left]
    return left_pointer


def quick_sort(array, left=0, right=None):
    if len(array) <= 1:
        return array
    if right is None:
        right = len(array)

    if left < right:
        pivot = (left + right) // 2
        array[pivot], array[left] = array[left], array[pivot]
        pivot = partition(array, left, right)
        random_quick_sort(array, left, pivot)
        random_quick_sort(array, pivot + 1, right)
    return array


def random_quick_sort(array, left=0, right=None):
    if len(array) <= 1:
        return array
    if right is None:
        right = len(array)

    if left < right:
        pivot = random.randint(left, right - 1)
        array[pivot], array[left] = array[left], array[pivot]
        pivot_index = partition(array, left, right)
        random_quick_sort(array, left, pivot_index)
        random_quick_sort(array, pivot_index + 1, right)
    return array


def partition3(array, left, right):
    pivot_value = array[left]
    left_pointer = left
    right_pointer = right - 1
    current_pointer = left + 1
    while current_pointer <= right_pointer:
        if array[current_pointer] < pivot_value:
            array[left_pointer], array[current_pointer] = array[current_pointer], array[left_pointer]
            left_pointer += 1
            current_pointer += 1
        elif array[current_pointer] > pivot_value:
            array[right_pointer], array[current_pointer] = array[current_pointer], array[right_pointer]
            right_pointer -= 1
        else:
            current_pointer += 1
    return left_pointer, right_pointer


def random_quick_sort3(array, left=0, right=None):
    if len(array) <= 1:
        return array
    if right is None:
        right = len(array)

    if left < right:
        pivot = random.randint(left, right - 1)
        array[pivot], array[left] = array[left], array[pivot]
        middle_left, middle_right = partition3(array, left, right)
        random_quick_sort3(array, left, middle_left)
        random_quick_sort3(array, middle_right + 1, right)
    return array

qsort = random_quick_sort

def qsort_plus_main():
    n, arr = file_read()
    sorted_array = qsort(arr)
    file_write(sorted_array)


if __name__ == '__main__':
    measure_performance(qsort_plus_main)