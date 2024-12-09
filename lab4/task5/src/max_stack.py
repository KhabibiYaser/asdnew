from lab4.utils import file_read, file_write, measure_performance
import os

class MaxStack:
    def __init__(self):
        self.stack = []  # Основной стек
        self.max_stack = []  # Стек для хранения максимумов

    def push(self, value):
        self.stack.append(value)
        # Добавляем новый максимум в max_stack
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)

    def pop(self):
        if not self.stack:
            return None
        value = self.stack.pop()
        # Убираем из max_stack, если удаляемое значение было максимумом
        if value == self.max_stack[-1]:
            self.max_stack.pop()
        return value

    def max(self):
        # Возвращаем текущий максимум
        return self.max_stack[-1] if self.max_stack else None


def process_max_stack():
    commands = file_read()  # Читаем команды из input.txt
    max_stack = MaxStack()
    results = []

    for command in commands:
        if command.startswith("push"):
            _, value = command.split()
            max_stack.push(int(value))
        elif command == "pop":
            max_stack.pop()
        elif command == "max":
            results.append(max_stack.max())

    file_write(results)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    measure_performance(process_max_stack)
