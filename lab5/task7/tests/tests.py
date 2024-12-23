import unittest
from lab5.task7.src.heap_sort import *
from lab5.utils import *


class TestHeapSort(unittest.TestCase):
    def test_sorted_array(self):
        # given
        array = [5, 3, 8, 4, 2]
        expected = [8, 5, 4, 3, 2]

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(heap_sort, array)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")

    def test_large_array(self):
        # given
        array = [i for i in range(1000, 0, -1)]
        expected = sorted(array, reverse=True)

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(heap_sort, array)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")

    def test_small_array(self):
        # given
        array = [3, 1, 2]
        expected = [3, 2, 1]

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(heap_sort, array)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")


if __name__ == "__main__":
    unittest.main()