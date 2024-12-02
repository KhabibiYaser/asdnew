# -*- coding: utf-8 -*-

import unittest
from lab1.task1.src.task1 import insertion_sort, sort_main
from lab1.utils import file_write


class TestTask1(unittest.TestCase):
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([31, 41, 59, 26, 41, 58]), [26, 31, 41, 41, 58, 59])
        self.assertEqual(insertion_sort([1]), [1])
        self.assertEqual(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

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
        self.assertEqual(result, "26 31 41 41 58 59")  # Ожидаемый результат

if __name__ == '__main__':
    unittest.main()

