import unittest

from lab3.task2.src.anti_qsort import *


class TestAntiQSort(unittest.TestCase):
    def test_should_antiqsort_small(self):
        # given
        number = 3
        expected = [1, 3, 2]

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(anti_qsort, number)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")

    def test_should_antiqsort_big(self):
        # given
        number = 10
        expected = [1, 4, 6, 8, 10, 5, 3, 7, 2, 9]

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(anti_qsort, number)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")


if __name__ == '__main__':
    unittest.main()
