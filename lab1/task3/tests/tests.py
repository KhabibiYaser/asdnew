import unittest
from lab1.task3.src.task3 import insertion_sort_descending, sort_main, recursive_insertion_sort_descending
from lab1.utils import file_write

class TestTask3(unittest.TestCase):
    def test_insertion_sort_descending(self):
        self.assertEqual(insertion_sort_descending([31, 41, 59, 26, 41, 58]), [59, 58, 41, 41, 31, 26])
        self.assertEqual(insertion_sort_descending([1]), [1])
        self.assertEqual(insertion_sort_descending([5, 4, 3, 2, 1]), [5, 4, 3, 2, 1])
        self.assertEqual(insertion_sort_descending([-1, -3, -2, 0]), [0, -1, -2, -3])

    def test_file_processing(self):
        # Пишем корректные тестовые данные в input.txt
        with open('../txtf/input.txt', 'w') as file:
            file.write("6\n")  # Размер массива
            file.write("31 41 59 26 41 58\n")  # Массив

        # Вызываем основную функцию
        sort_main()

        # Проверяем результат в output.txt
        with open('../txtf/output.txt', 'r') as file:
            result = file.read().strip()
        self.assertEqual(result, "59 58 41 41 31 26")  # Ожидаемый результат

    def test_recursive_insertion_sort_descending(self):
        arr = [31, 41, 59, 26, 41, 58]
        recursive_insertion_sort_descending(arr, len(arr))
        self.assertEqual(arr, [59, 58, 41, 41, 31, 26])

        arr = [5, 4, 3, 2, 1]
        recursive_insertion_sort_descending(arr, len(arr))
        self.assertEqual(arr, [5, 4, 3, 2, 1])

if __name__ == '__main__':
    unittest.main()
