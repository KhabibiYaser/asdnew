import os
import sys
from lab5.utils import file_read, file_write, measure_performance

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)


def is_heap(arr):
    """Проверяет, является ли массив неубывающей пирамидой."""
    n = len(arr)
    for i in range(n // 2):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] > arr[left]:
            return "NO"
        if right < n and arr[i] > arr[right]:
            return "NO"
    return "YES"


def process_is_heap():
    """Читает данные, проверяет массив и записывает результат."""
    data = file_read()
    n = int(data[0][0])
    arr = list(map(int, data[1]))
    result = is_heap(arr)
    file_write([result])


if __name__ == "__main__":
    measure_performance(process_is_heap)
