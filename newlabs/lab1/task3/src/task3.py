from lab1.utils import *
import os , sys
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)


def swap(arr, i, j):
    """
    Меняет элементы массива местами.
    """
    arr[i], arr[j] = arr[j], arr[i]


def insertion_sort_descending(arr):
    """
    Итеративная сортировка вставками в порядке убывания с использованием swap.
    """
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] > arr[j - 1]:  # Условие для убывания
            swap(arr, j, j - 1)
            j -= 1
    return arr


def recursive_insertion_sort_descending(arr, n):
    """
    Рекурсивная сортировка вставками в порядке убывания.
    """
    # Базовый случай
    if n <= 1:
        return

    # Сортируем первые n-1 элементов
    recursive_insertion_sort_descending(arr, n - 1)

    # Вставляем последний элемент на правильное место
    last = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] < last:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = last


def sort_main():
    """
    Главная функция для чтения данных, сортировки и записи результата.
    """
    _, arr = file_read_size_int_array()  # Читаем данные
    if not (1 <= len(arr) <= 10 ** 3):
        raise ValueError("Размер массива должен быть в пределах 1 <= n <= 10^3")
    if any(abs(x) > 10 ** 9 for x in arr):
        raise ValueError("Все элементы массива должны быть по модулю не больше 10^9")

    # Выбор варианта сортировки: итеративный или рекурсивный
    sorted_arr = insertion_sort_descending(arr)  # Итеративная сортировка
    recursive_insertion_sort_descending(arr, len(arr))  # Рекурсивная сортировка (раскомментировать при необходимости)

    file_write(arr)  # Записываем результат в файл


if __name__ == '__main__':
    measure_performance(sort_main)
