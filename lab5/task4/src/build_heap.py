import os
import sys
from lab5.utils import file_read, file_write, measure_performance

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)


def build_heap(data):
    """Преобразует массив в min-heap и возвращает список перестановок."""
    n = len(data)
    swaps = []

    def sift_down(i):
        min_index = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and data[left] < data[min_index]:
            min_index = left
        if right < n and data[right] < data[min_index]:
            min_index = right

        if i != min_index:
            swaps.append((i, min_index))
            data[i], data[min_index] = data[min_index], data[i]
            sift_down(min_index)

    for i in range(n // 2 - 1, -1, -1):
        sift_down(i)

    return swaps


def process_build_heap():
    """Читает данные, строит пирамиду и записывает результат."""
    data = file_read()
    n = int(data[0][0])
    arr = list(map(int, data[1]))
    swaps = build_heap(arr)
    output = [len(swaps)] + [f"{i} {j}" for i, j in swaps]
    file_write(output)


if __name__ == "__main__":
    measure_performance(process_build_heap)
