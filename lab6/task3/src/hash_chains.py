import os
import sys
from lab6.utils import  *

# Настройка пути
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)


class HashTable:
    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.table = [[] for _ in range(bucket_count)]

    def _hash_function(self, string):
        """
        Полиномиальная хеш-функция.
        """
        p = 1000000007
        x = 263
        hash_value = 0
        for i, c in enumerate(string):
            hash_value += ord(c) * (x ** i)
            hash_value %= p
        return hash_value % self.bucket_count

    def add(self, string):
        """
        Добавление строки в хеш-таблицу.
        """
        index = self._hash_function(string)
        if string not in self.table[index]:
            self.table[index].insert(0, string)

    def delete(self, string):
        """
        Удаление строки из хеш-таблицы.
        """
        index = self._hash_function(string)
        if string in self.table[index]:
            self.table[index].remove(string)

    def find(self, string):
        """
        Проверка наличия строки в хеш-таблице.
        """
        index = self._hash_function(string)
        return "yes" if string in self.table[index] else "no"

    def check(self, i):
        """
        Возвращает содержимое сегмента хеш-таблицы в обратном порядке добавления.
        """
        if 0 <= i < self.bucket_count:
            return " ".join(self.table[i][::-1])  # Возвращаем список в обратном порядке
        return ""


def process_hash_table(data):
    """
    Обработка запросов для хеш-таблицы.
    """
    bucket_count = int(data[0])
    queries = data[1:]

    # Создаём хеш-таблицу
    hash_table = HashTable(bucket_count)
    results = []

    # Обрабатываем запросы
    for query in queries:
        parts = query.split()
        command = parts[0]

        if command == "add":
            hash_table.add(parts[1])
        elif command == "del":
            hash_table.delete(parts[1])
        elif command == "find":
            results.append(hash_table.find(parts[1]))
        elif command == "check":
            results.append(hash_table.check(int(parts[1])))

    return results


if __name__ == '__main__':
    # Читаем входные данные и передаем их в process_hash_table
    data = file_read()
    result = measure_performance(process_hash_table, data)
    file_write(result[0])  # Только результат передается в file_write

