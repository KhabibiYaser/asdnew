# -*- coding: utf-8 -*-
from lab0.task1.src.task2 import sum_with_square
from lab0.utils import *
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)


def sum_with_square_from_file():
    """
    Читает два числа из файла input.txt, вычисляет a + b^2 и записывает результат в output.txt.
    """
    _, arr = file_read_size_int_array()
    if len(arr) != 2:
        raise ValueError("Файл должен содержать ровно два числа.")
    a, b = arr
    result = sum_with_square(a, b)
    file_write([result])
