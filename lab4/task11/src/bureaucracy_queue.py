from lab4.utils import file_read, file_write, measure_performance
import os

def process_queue(n, m, demands):
    queue = list(demands)  # Очередь только с требованиями справок

    while m > 0 and queue:
        current = queue.pop(0)  # Берем первого в очереди
        if current > 1:
            queue.append(current - 1)
        m -= 1

    # Если очередь пуста, возвращаем -1
    if not queue:
        return ["-1"]
    else:
        return [str(len(queue))] + [" ".join(map(str, queue))]


def process_bureaucracy():
    data = file_read()
    n, m = map(int, data[0].split())
    demands = list(map(int, data[1].split()))
    result = process_queue(n, m, demands)
    file_write(result)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    measure_performance(process_bureaucracy)
