import unittest
from lab3.task6.src.zahlen_sort import *


class TestZahlenSort(unittest.TestCase):
    def check_zahlen_sort(self, filename, expected):
        n, m, array_a, array_b = file_read_int_int_array_array(filename)
        combinations = multiply(n, m, array_a, array_b)
        result, elapsed_time, peak_memory_megabytes = measure_performance(sum_tenth, combinations)
        self.assertEqual(result, expected)


    def test_should_zahlen_sort_example_a(self):
        filename = '../txtf/test_input1.txt'
        self.check_zahlen_sort(filename, 51)


    def test_should_zahlen_sort_example_b(self):
        filename = '../txtf/test_input2.txt'
        self.check_zahlen_sort(filename, 3)


    def test_should_zahlen_sort_example_c(self):
        filename = '../txtf/test_input3.txt'
        self.check_zahlen_sort(filename, 0)


if __name__ == '__main__':
    unittest.main()
