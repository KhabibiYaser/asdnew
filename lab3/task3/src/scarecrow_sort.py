from lab3.utils import *
from lab3.task1.src.qsort_plus import qsort

import os,sys
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)


def can_sort_dolls(dolls_number, hand, dolls):
    groups = [[] for _ in range(hand)]

    for i in range(dolls_number):
        groups[i % hand].append(dolls[i])

    for group in groups:
        qsort(group)

    sorted_dolls = []
    index = [0] * hand

    for i in range(dolls_number):
        group_index = i % hand
        sorted_dolls.append(groups[group_index][index[group_index]])
        index[group_index] += 1

    if sorted_dolls == qsort(dolls):
        return "YES"
    return "NO"


def scarecrow_sort_main():
    (n, k), array = file_read()
    result = can_sort_dolls(n, k, array)
    file_write([result])


if __name__ == '__main__':
    measure_performance(scarecrow_sort_main)