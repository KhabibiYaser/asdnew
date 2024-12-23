import os
import sys
import subprocess
import random
import time
import tracemalloc
from typing import Tuple, Generator, Type
from inspect import stack
from pathlib import Path

# Настройка рабочей директории и пути
def setup_working_directory():
    """
    Устанавливает рабочую директорию на директорию текущего файла и добавляет её в sys.path.
    """
    abspath = Path(__file__).resolve()
    dname = abspath.parent
    sys.path.append(str(dname))
    os.chdir(dname)

setup_working_directory()


def get_calling_file_path() -> Path:
    """
    Возвращает абсолютный путь к файлу, который вызвал текущую функцию.
    """
    file_path = stack()[2].filename
    return Path(file_path).resolve()


def read(filename: str = '../txtf/input.txt', type_convert: Type = int) -> Generator[list, None, None]:
    """
    Читает файл построчно с преобразованием типов.

    :param filename: Относительный путь к файлу для чтения.
    :param type_convert: Тип, в который будут конвертированы данные (по умолчанию int).
    :return: Генератор списков строк или преобразованных типов.
    """
    file_path = Path(get_calling_file_path()).parent / filename

    try:
        with file_path.open('r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split()
                if not parts:
                    continue
                if type_convert is not str:
                    try:
                        parts = [type_convert(part) for part in parts]
                    except ValueError as e:
                        print(f"Ошибка конвертации строки: {e}")
                        continue
                yield parts
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла {file_path}: {e}")


def write(*values, sep: str = " ", end: str = "\n", filename: str = '../txtf/output.txt',
          to_end: bool = False) -> None:
    """
    Записывает данные в файл.

    :param values: Данные для записи.
    :param sep: Разделитель между данными.
    :param end: Строка, которая будет добавлена в конце.
    :param filename: Относительный путь к файлу для записи.
    :param to_end: Если True, данные будут добавлены в конец файла, иначе файл будет перезаписан.
    """
    file_path = Path(get_calling_file_path()).parent / filename
    mode = 'a' if to_end else 'w'

    try:
        with file_path.open(mode, encoding='utf-8') as file:
            print(*values, sep=sep, end=end, file=file)
    except Exception as e:
        print(f"Произошла ошибка при записи в файл {file_path}: {e}")


def time_data(func) -> float:
    """
    Измеряет время выполнения функции.

    :param func: Функция для измерения времени выполнения.
    :return: Время выполнения в секундах.
    """
    time_start = time.perf_counter()
    func()
    elapsed = time.perf_counter() - time_start
    print(f"Время выполнения {func.__name__}: {elapsed:.6f} секунд")
    return elapsed


def memory_data(func) -> Tuple[float, float]:
    """
    Измеряет потребление памяти функцией.

    :param func: Функция для измерения потребления памяти.
    :return: Кортеж с текущей и пиковой памятью в МБ.
    """
    tracemalloc.start()
    func()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    current_mb = current / (1024 ** 2)
    peak_mb = peak / (1024 ** 2)
    print(f"Потребление памяти {func.__name__}: текущее {current_mb:.2f} МБ, пиковое {peak_mb:.2f} МБ")
    return current_mb, peak_mb


def run_tasks(working_dir: str, root_dir: str) -> None:
    """
    Запускает задачи из заданной директории.

    :param working_dir: Директория с задачами.
    :param root_dir: Корневая директория для запуска скриптов.
    """
    working_path = Path(working_dir)
    root_path = Path(root_dir)

    for task_dir in working_path.iterdir():
        if task_dir.is_dir() and task_dir.name.startswith('task'):
            src_dir = task_dir / 'src'
            for py_file in src_dir.rglob('*.py'):
                run_path = py_file.relative_to(root_path)
                print('—————————————————————————————————————————————')
                print(f'RUNNING {run_path}')
                try:
                    subprocess.run(['python', str(py_file)], cwd=root_path, check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Ошибка при выполнении {run_path}: {e}")

            txtf_dir = task_dir / 'txtf'
            input_file = txtf_dir / 'input.txt'
            output_file = txtf_dir / 'output.txt'

            if input_file.exists():
                print('---------------------------------------------')
                print('ВХОДНЫЕ ДАННЫЕ')
                for line in read(input_file.relative_to(root_path), type_convert=str):
                    print(*line)
            else:
                print(f"Файл {input_file} не найден.")

            if output_file.exists():
                print('---------------------------------------------')
                print('ВЫХОДНЫЕ ДАННЫЕ')
                for line in read(output_file.relative_to(root_path), type_convert=str):
                    print(*line)
            else:
                print(f"Файл {output_file} не найден.")


def generate_random_array(n: int, left: int, right: int) -> list:
    """
    Генерирует массив случайных чисел.

    :param n: Количество элементов в массиве.
    :param left: Нижняя граница диапазона.
    :param right: Верхняя граница диапазона.
    :return: Список случайных чисел.
    """
    array = [random.randint(left, right) for _ in range(n)]
    return array


# Пример использования (можно убрать или оставить для тестирования)
if __name__ == "__main__":
    # Пример генерации массива
    arr = generate_random_array(10, 1, 100)
    print(f"Сгенерированный массив: {arr}")

    # Пример записи в файл
    write("Пример", "записи", "в", "файл")

    # Пример чтения из файла
    for line in read('../txtf/input.txt', type_convert=str):
        print(line)

    # Пример замеров времени и памяти
    def sample_function():
        return sum(generate_random_array(1000000, 1, 100))

    time_data(sample_function)
    memory_data(sample_function)

    # Пример запуска задач
    # run_tasks('path_to_working_dir', 'path_to_root_dir')
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
    with open(output_file_path, 'w') as file:
        output = " ".join(map(str, writing))
        file.write(output)
        print('Output:', output, sep='\n')