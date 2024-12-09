from lab4.utils import file_read, file_write, measure_performance

import os

def check_brackets(sequence):
    stack = []
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}

    for i, char in enumerate(sequence):
        if char in bracket_pairs:  # Открывающая скобка
            stack.append((char, i + 1))
        elif char in bracket_pairs.values():  # Закрывающая скобка
            if not stack:
                return i + 1
            top, pos = stack.pop()
            if bracket_pairs[top] != char:
                return i + 1

    if stack:
        _, pos = stack.pop()
        return pos

    return "Success"


def process_brackets():
    data = file_read()
    result = check_brackets(data[0])
    file_write([result])


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    measure_performance(process_brackets)
