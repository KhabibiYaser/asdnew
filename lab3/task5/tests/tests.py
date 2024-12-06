import unittest

from lab3.task5.src.hirsh_index import *


class TestHirshIndex(unittest.TestCase):
    def test_should_example_a(self):
        # given
        line = [0]
        expected = 0

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(hirsh_index, line)

        # then
        self.assertEqual(result, expected)
        # self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        # self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")
        # Performance check wasn't requested in the task.

    def test_should_example_b(self):
        # given
        line = [1, 3, 1]
        expected = 1

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(hirsh_index, line)

        # then
        self.assertEqual(result, expected)
        # self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        # self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")
        # Performance check wasn't requested in the task.

    def test_should_example_c(self):
        # given
        line = [3, 0, 6, 1, 5]
        expected = 3

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(hirsh_index, line)

        # then
        self.assertEqual(result, expected)
        # self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        # self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")
        # Performance check wasn't requested in the task.


if __name__ == '__main__':
    unittest.main()
