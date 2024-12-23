import os
import sys
from lab5.utils import file_read, file_write, measure_performance

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)


def max_heapify(arr, n, i):
    """Итеративный Max-Heapify для обеспечения свойств кучи."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    while True:
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest
            left = 2 * i + 1
            right = 2 * i + 2
        else:
            break


def heap_sort(arr):
    """Реализация пирамидальной сортировки."""
    n = len(arr)

    # Построение max-кучи
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

    # Извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, i, 0)

    # Возвращаем массив в порядке убывания
    return arr[::-1]


def process_heap_sort():
    """Читает данные, сортирует массив и записывает результат."""
    data = file_read()
    n = int(data[0][0])
    arr = list(map(int, data[1]))
    sorted_arr = heap_sort(arr)
    file_write([" ".join(map(str, sorted_arr))])


if __name__ == "__main__":
    measure_performance(process_heap_sort)
