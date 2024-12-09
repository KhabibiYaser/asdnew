from lab4.utils import read_stack_input, write_output, measure_performance
import os


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        value = self.top.value
        self.top = self.top.next
        return value

    def __str__(self):
        elements = []
        current = self.top
        while current:
            elements.append(current.value)
            current = current.next
        return " -> ".join(map(str, elements))


def process_stack():
    commands = read_stack_input()
    stack = LinkedStack()
    results = []

    for command in commands:
        if command.startswith("push"):
            _, value = command.split()
            stack.push(int(value))
        elif command == "pop":
            try:
                results.append(stack.pop())
            except IndexError:
                results.append("error")
        elif command == "isEmpty":
            results.append("true" if stack.isEmpty() else "false")

    write_output(results)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    measure_performance(process_stack)
