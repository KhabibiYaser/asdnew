import os
from lab4.utils import file_read, file_write, measure_performance


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop() if self.stack else None


def process_stack_commands(commands):
    stack = Stack()  # Инициализация стека
    results = []

    for command in commands:
        if command.startswith('+'):
            _, value = command.split()
            stack.push(int(value))
        elif command == '-':
            results.append(stack.pop())

    return results


if __name__ == '__main__':
    # Смена текущей директории на директорию файла stack.py
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    commands = file_read()
    result = measure_performance(process_stack_commands, commands)
    file_write(result[0])


