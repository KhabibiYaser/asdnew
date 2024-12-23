import unittest

from lab5.task1.src.is_heap import is_heap
from lab5.utils import measure_performance



class TestIsHeap(unittest.TestCase):
    def test_heap_valid(self):
        # given
        array = [1, 2, 3, 4, 5]
        expected = "YES"

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(is_heap, array)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")

    def test_heap_invalid(self):
        # given
        array = [5, 1, 0, 1, 2, 0]
        expected = "NO"

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(is_heap, array)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")

    def test_heap_edge_case(self):
        # given
        array = [10]
        expected = "YES"

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(is_heap, array)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")


if __name__ == "__main__":
    unittest.main()
