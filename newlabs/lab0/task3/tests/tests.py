import unittest
from lab0.task3.src.task3 import last_digit_of_fib, last_digit_main
from lab0.utils import file_write, file_read_size_int_array


class TestTask3(unittest.TestCase):
    def test_valid_numbers(self):
        self.assertEqual(last_digit_of_fib(0), 0)
        self.assertEqual(last_digit_of_fib(1), 1)
        self.assertEqual(last_digit_of_fib(331), 9)
        self.assertEqual(last_digit_of_fib(327305), 5)

    def test_out_of_range(self):
        with self.assertRaises(ValueError):
            last_digit_of_fib(-1)

    def test_file_processing(self):
        # Пишем тестовые данные в input.txt
        file_write([331], '../txtf/input.txt')

        # Вызываем основную функцию
        last_digit_main()

        # Проверяем результат в output.txt
        with open('../txtf/output.txt', 'r') as file:
            result = file.read().strip()
        self.assertEqual(result, "9")


if __name__ == '__main__':
    unittest.main()
