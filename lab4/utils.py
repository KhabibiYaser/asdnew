import time
import tracemalloc


def measure_performance(function, *args, **kwargs):
    start_time = time.perf_counter()
    tracemalloc.start()

    result = function(*args, **kwargs)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    peak_memory_megabytes = peak / 10 ** 6

    print(f"Execution time: {elapsed_time:.6f} seconds")
    print(f"Peak memory usage: {peak_memory_megabytes:.6f} MB")

    return result, elapsed_time, peak_memory_megabytes


def file_read(input_file_path='../txtf/input.txt'):
    """
    Универсальная функция чтения входных данных из файла.
    """
    with open(input_file_path, 'r') as file:
        lines = file.read().splitlines()
        print("Input:")
        for line in lines:
            print(line)
    return lines


def file_write(writing, output_file_path='../txtf/output.txt'):
    """
    Универсальная функция записи выходных данных в файл.
    """
    with open(output_file_path, 'w') as file:
        for line in writing:
            file.write(f"{line}\n")
        print("Output:")
        for line in writing:
            print(line)


# Новые функции для задачи 13

def read_stack_input():
    """
    Читает входные данные для задачи стека из test_input_stack.txt.
    """
    input_file_path = '../txtf/test_input_stack.txt'
    with open(input_file_path, 'r') as file:
        lines = file.read().splitlines()
        print("Stack Input:")
        for line in lines:
            print(line)
    return lines

# Добавить ограничение по времени по памяти в тех тзаджачах где это нужно , использовать assertLessequal

def read_queue_input():
    """
    Читает входные данные для задачи очереди из test_input_queue.txt.
    """
    input_file_path = '../txtf/test_input_queue.txt'
    with open(input_file_path, 'r') as file:
        lines = file.read().splitlines()
        print("Queue Input:")
        for line in lines:
            print(line)
    return lines


def write_output(results):
    """
    Записывает выходные данные в output.txt (задача 13).
    """
    output_file_path = '../txtf/output.txt'
    with open(output_file_path, 'w') as file:
        for line in results:
            file.write(f"{line}\n")
        print("Output:")
        for line in results:
            print(line)
