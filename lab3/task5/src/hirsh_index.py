from lab3.utils import *
from lab3.task1.src.qsort_plus import qsort

import os,sys
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)


def hirsh_index(citations):
    qsort(citations)
    citations.reverse()

    h = 0
    for i in range(len(citations)):
        if citations[i] > i:
            h += 1
        else:
            break
    return h


def hirsh_index_main():
    (line,) = file_read()
    result = hirsh_index(line)
    file_write([result])


if __name__ == '__main__':
    measure_performance(hirsh_index_main)