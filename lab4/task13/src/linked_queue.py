from lab4.utils import read_queue_input, write_output, measure_performance
import os


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def __str__(self):
        elements = []
        current = self.front
        while current:
            elements.append(current.value)
            current = current.next
        return " <- ".join(map(str, elements))


def process_queue():
    commands = read_queue_input()
    queue = LinkedQueue()
    results = []

    for command in commands:
        if command.startswith("enqueue"):
            _, value = command.split()
            queue.enqueue(int(value))
        elif command == "dequeue":
            try:
                results.append(queue.dequeue())
            except IndexError:
                results.append("error")
        elif command == "isEmpty":
            results.append("true" if queue.isEmpty() else "false")

    write_output(results)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    measure_performance(process_queue)

