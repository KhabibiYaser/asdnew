import sys
import time
import tracemalloc
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)


def measure_performance(function, *args, **kwargs):
    """
    Измеряет время выполнения и пиковое использование памяти.
    """
    start_time = time.perf_counter()
    tracemalloc.start()

    result = function(*args, **kwargs)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    peak_memory_megabytes = peak / 10 ** 6  # переводим в мегабайты

    print(f"Execution time: {elapsed_time:.6f} seconds")
    print(f"Peak memory usage: {peak_memory_megabytes:.6f} MB")

    return result, elapsed_time, peak_memory_megabytes


def file_read_size_int_array(input_file_path='../txtf/input.txt'):
    """
    Универсальная функция чтения данных из файла.
    Поддерживает формат:
    1. Одна строка с числами.
    2. Две строки: первая строка - размер массива, вторая - числа массива.
    """
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

        if not lines:
            raise ValueError("Файл пустой. Пожалуйста, добавьте данные в input.txt.")

        # Если файл содержит только одну строку с числами
        if len(lines) == 1:
            array = list(map(int, lines[0].strip().split()))
            return len(array), array

        # Если файл содержит первую строку как размер массива
        elif len(lines) >= 2:
            n = int(lines[0].strip())
            array = list(map(int, lines[1].strip().split()))
            return n, array

        else:
            raise ValueError("Некорректный формат файла input.txt.")


def file_write(writing, output_file_path='../txtf/output.txt'):
    """
    Записывает данные в файл в одну строку.
    """
    with open(output_file_path, 'w') as file:
        file.write(" ".join(map(str, writing)))
