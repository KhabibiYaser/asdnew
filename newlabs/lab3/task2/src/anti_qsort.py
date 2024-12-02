from lab3.utils import *
import os,sys
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)


def anti_qsort(numbers):
    res = list(range(1, numbers + 1))
    for i in range(2, numbers):
        res[i // 2], res[i] = res[i], res[i // 2]
    return res


def anti_qsort_main():
    n = file_read_size_int_single()
    answer = anti_qsort(n)
    file_write(answer)


if __name__ == "__main__":
    measure_performance(anti_qsort_main)