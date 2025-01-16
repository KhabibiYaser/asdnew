from lab7.utils import measure_performance,file_write,file_read
import os, sys

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)

def optimal_sequence(n):
    """
    Вычисляет минимальное количество операций для достижения числа n из 1
    и возвращает последовательность промежуточных значений.
    """
    operations = [0] * (n + 1)

    for i in range(2, n + 1):
        min_ops = operations[i - 1] + 1
        if i % 2 == 0:
            min_ops = min(min_ops, operations[i // 2] + 1)
        if i % 3 == 0:
            min_ops = min(min_ops, operations[i // 3] + 1)
        operations[i] = min_ops

    sequence = []
    while n > 0:
        sequence.append(n)
        if n % 3 == 0 and operations[n] == operations[n // 3] + 1:
            n //= 3
        elif n % 2 == 0 and operations[n] == operations[n // 2] + 1:
            n //= 2
        else:
            n -= 1

    return operations[-1], sequence[::-1]


def primitive_calculator_main():
    n = file_read()[0][0]  # Чтение числа n
    min_ops, sequence = optimal_sequence(n)
    file_write([min_ops, sequence])


if __name__ == '__main__':
    measure_performance(primitive_calculator_main)


