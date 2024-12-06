# -*- coding: utf-8 -*-
from lab0.utils import *
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)

def sum_of_nums(a, b):
    """
    Функция вычисляет сумму двух чисел.
    Проверяет соблюдение диапазона чисел: -10^9 <= a, b <= 10^9.
    """
    if -10 ** 9 <= a <= 10 ** 9 and -10 ** 9 <= b <= 10 ** 9:
        return a + b
    else:
        raise ValueError("Числа должны быть в диапазоне -10^9 <= x, y <= 10^9.")
