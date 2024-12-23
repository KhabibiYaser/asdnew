from lab5.utils import file_read, file_write, measure_performance

import os , sys
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)

def calculate_tree_height(n, parents):
    """Вычисляет высоту дерева."""
    children = [[] for _ in range(n)]
    root = -1

    for child_index, parent_index in enumerate(parents):
        if parent_index == -1:
            root = child_index
        else:
            children[parent_index].append(child_index)

    def compute_height(node):
        if not children[node]:
            return 1
        return 1 + max(compute_height(child) for child in children[node])

    return compute_height(root)

def process_tree_height():
    """Функция для обработки данных дерева."""
    data = file_read()
    n = int(data[0][0])  # Первое значение - количество узлов
    parents = list(map(int, data[1]))  # Вторая строка - массив родителей
    height = calculate_tree_height(n, parents)
    file_write([height])

if __name__ == "__main__":
    measure_performance(process_tree_height)