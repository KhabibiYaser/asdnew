import unittest
import random
from itertools import accumulate

from lab2.task7.src.max_subarray_search_in_linear_time import *


# helper
def answer(testlist):
    return max(accumulate(testlist, lambda x, y: max(y, x + y)))


class TestMaxSubarray(unittest.TestCase):
    def test_should_empty(self):
        # given
        testlist = []

        # when
        try:
            kadane(testlist)
        except ValueError as e:
            exception_raised = True
            exception = e
        else:
            exception_raised = False
            exception = None

        # then
        self.assertTrue(exception_raised, "Expected TypeError was not raised.")
        self.assertIsInstance(exception, ValueError, "Exception raised was not a TypeError.")

    def test_should_random(self):
        # given
        testlist = [random.randint(-10 ** 9, 10 ** 9) for _ in range(random.randint(1, 20000))]
        expected = answer(testlist)

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(kadane, testlist)

        # then
        self.assertEqual(result[2], expected)
        # self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        # self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")
        # Performance check wasn't requested in the task.

    def test_should_max_size(self):
        # given
        testlist = [random.randint(-10 ** 9, 10 ** 9) for _ in range(20000)]
        expected = answer(testlist)

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(kadane, testlist)

        # then
        self.assertEqual(result[2], expected)
        # self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        # self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")
        # Performance check wasn't requested in the task.

    def test_should_max_size_reverse_sorted(self):
        # given
        testlist = [random.randint(-10 ** 9, 10 ** 9) for _ in range(20000)]
        testlist.sort(reverse=True)
        expected = answer(testlist)

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(kadane, testlist)

        # then
        self.assertEqual(result[2], expected)
        # self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        # self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")
        # Performance check wasn't requested in the task.

    def test_should_huge_numbers(self):
        # given
        testlist = [1000000000, 999999999, 999999998]
        expected = answer(testlist)

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(kadane, testlist)

        # then
        self.assertEqual(result[2], expected)
        # self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        # self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")
        # Performance check wasn't requested in the task.

    def test_should_not_list(self):
        # given
        testdata = 2

        # when
        try:
            kadane(testdata)
        except TypeError as e:
            exception_raised = True
            exception = e
        else:
            exception_raised = False
            exception = None

        # then
        self.assertTrue(exception_raised, "Expected TypeError was not raised.")
        self.assertIsInstance(exception, TypeError, "Exception raised was not a TypeError.")


if __name__ == '__main__':
    unittest.main()
