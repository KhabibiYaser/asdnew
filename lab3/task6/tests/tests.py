import unittest

from lab3.task6.src.zahlen_sort import *


class TestZahlenSort(unittest.TestCase):
    def test_should_zahlen_sort_example_a(self):
        # given
        (n, m), array_a, array_b = (4, 4), [7, 1, 4, 9], [2, 7, 8, 11]
        expected = 51

        # when
        combinations = multiply(n, m, array_a, array_b)
        result, elapsed_time, peak_memory_megabytes = measure_performance(sum_tenth, combinations)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 512, "Memory usage exceeded 512 MB")

    def test_should_zahlen_sort_example_b(self):
        # given
        (n, m), array_a, array_b = (2, 2), [1, 2], [3, 4]
        expected = 3

        # when
        combinations = multiply(n, m, array_a, array_b)
        result, elapsed_time, peak_memory_megabytes = measure_performance(sum_tenth, combinations)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 512, "Memory usage exceeded 512 MB")

    def test_should_zahlen_sort_example_c(self):
        # given
        (n, m), array_a, array_b = (1, 1), [0], [99]
        expected = 0

        # when
        combinations = multiply(n, m, array_a, array_b)
        result, elapsed_time, peak_memory_megabytes = measure_performance(sum_tenth, combinations)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 512, "Memory usage exceeded 512 MB")


if __name__ == '__main__':
    unittest.main()
