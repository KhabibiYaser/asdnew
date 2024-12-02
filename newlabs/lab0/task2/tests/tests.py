# -*- coding: utf-8 -*-
import unittest
from lab0.task2.src.task2 import calc_fib, fibonacci_main
from lab0.utils import file_write, file_read_size_int_array



class TestTask2(unittest.TestCase):
    def test_valid_numbers(self):
        self.assertEqual(calc_fib(0), 0)
        self.assertEqual(calc_fib(1), 1)
        self.assertEqual(calc_fib(10), 55)
        self.assertEqual(calc_fib(45), 1134903170)

    def test_out_of_range(self):
        with self.assertRaises(ValueError):
            calc_fib(-1)

    def test_file_processing(self):
        # Пишем тестовые данные в input.txt
        file_write([10], '../txtf/input.txt')

        # Вызываем основную функцию
        fibonacci_main()

        # Проверяем результат в output.txt
        with open('../txtf/output.txt', 'r') as file:
            result = file.read().strip()
        self.assertEqual(result, "55")


if __name__ == '__main__':
    unittest.main()
