import unittest
from lab1.task6.src.task6 import bubble_sort, sort_main
from lab1.utils import file_write

class TestTask6(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([31, 41, 59, 26, 41, 58]), [26, 31, 41, 41, 58, 59])
        self.assertEqual(bubble_sort([1]), [1])
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([-1, -3, -2, 0]), [-3, -2, -1, 0])

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
        self.assertEqual(result, "26 31 41 41 58 59")  # Ожида
