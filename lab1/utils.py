import os
import time
import tracemalloc
import os , sys
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


def get_absolute_path(relative_path):
    """
    Преобразует относительный путь в абсолютный относительно текущей рабочей директории.
    """
    caller_dir = os.getcwd()
    return os.path.abspath(os.path.join(caller_dir, relative_path))


def file_read_size_int_array(input_file_path='../txtf/input.txt'):
    """
    Читает данные из файла.
    Первая строка - размер массива n.
    Вторая строка - массив из n элементов.
    """
    input_file_path = get_absolute_path(input_file_path)
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"Файл {input_file_path} не найден.")

    with open(input_file_path, 'r') as file:
        lines = file.readlines()

        if len(lines) < 2:
            raise ValueError("Файл должен содержать две строки: размер массива и сам массив.")

        n = int(lines[0].strip())
        array = list(map(int, lines[1].strip().split()))

        if len(array) != n:
            raise ValueError("Размер массива не совпадает с указанным значением n.")

        return n, array


def file_read_binary_numbers(input_file_path='../txtf/input.txt'):
    """
    Читает два двоичных числа из файла.
    Ожидает, что файл содержит ровно две строки с n-битовыми числами.
    """
    input_file_path = get_absolute_path(input_file_path)
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"Файл {input_file_path} не найден.")

    with open(input_file_path, 'r') as file:
        lines = file.readlines()

        # Проверяем, что файл содержит ровно две строки
        if len(lines) != 2:
            raise ValueError("Файл должен содержать ровно две строки: два n-битовых числа.")

        # Преобразуем строки в списки целых чисел
        a = list(map(int, lines[0].strip()))
        b = list(map(int, lines[1].strip()))

        return a, b


def file_write(writing, output_file_path='../txtf/output.txt', line_by_line=False):
    """
    Записывает данные в файл.
    Если line_by_line=True, записывает каждый элемент на новой строке.
    """
    output_file_path = get_absolute_path(output_file_path)
    with open(output_file_path, 'w') as file:
        if line_by_line:
            for line in writing:
                file.write(line + "\n")
        else:
            file.write(" ".join(map(str, writing)))
