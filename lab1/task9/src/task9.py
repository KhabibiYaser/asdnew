from lab1.utils import *

import os , sys
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)

def binary_addition(a, b):
    """
    Складывает два двоичных числа, заданных в виде массивов.
    Возвращает (n+1)-битовый массив.
    """
    n = len(a)
    c = [0] * (n + 1)  # Результат (n+1)-битовый массив
    carry = 0  # Перенос

    for i in range(n - 1, -1, -1):  # Проходим массивы справа налево
        total = a[i] + b[i] + carry
        c[i + 1] = total % 2  # Текущий бит
        carry = total // 2  # Перенос

    c[0] = carry  # Старший бит
    return c

def binary_addition_main():
    """
    Главная функция для чтения данных, сложения и записи результата.
    """
    a, b = file_read_binary_numbers()  # Читаем два числа
    if len(a) != len(b):
        raise ValueError("Числа должны быть одной длины.")
    if not (1 <= len(a) <= 10**3):
        raise ValueError("Длина числа должна быть в пределах 1 <= n <= 1000.")

    result = binary_addition(a, b)  # Складываем числа
    file_write(result, line_by_line=False)  # Записываем результат в файл одной строкой

if __name__ == '__main__':
    measure_performance(binary_addition_main)

