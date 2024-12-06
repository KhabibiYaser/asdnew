import unittest

from lab3.task3.src.scarecrow_sort import *


class TestScarecrowSort(unittest.TestCase):
    def test_example_a(self):
        # given
        (n, k), array = (3, 2), [2, 1, 3]
        expected = "NO"

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(can_sort_dolls, n, k, array)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")

    def test_example_b(self):
        # given
        (n, k), array = (5, 3), [1, 5, 3, 4, 1]
        expected = "YES"

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(can_sort_dolls, n, k, array)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")

    def test_example_c(self):
        # given
        (n, k), array = (7, 5), [1, 2, 4, 3, 5, 6, 7]
        expected = "NO"

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(can_sort_dolls, n, k, array)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")


if __name__ == '__main__':
    unittest.main()
