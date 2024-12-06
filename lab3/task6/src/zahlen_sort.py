from lab3.utils import *
from lab3.task1.src.qsort_plus import qsort

import os,sys
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)


def sum_tenth(combinations):
    qsort(combinations)
    return sum(combinations[i] for i in range(0, len(combinations), 10))


def multiply(n, m, array1, array2):
    combinations = []
    for i in range(n):
        for j in range(m):
            combinations.append(array1[i] * array2[j])
    return combinations


def solve(n, m, array1, array2):
    combinations = multiply(n, m, array1, array2)
    result = sum_tenth(combinations)
    return result


def zahlen_sort_main():
    (n, m), array_a, array_b = file_read()
    result = solve(n, m, array_a, array_b)
    file_write([result])


if __name__ == '__main__':
    measure_performance(zahlen_sort_main)

