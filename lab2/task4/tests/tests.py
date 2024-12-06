# -*- coding: utf-8 -*-
import unittest

from lab2.task4.src.binary_search import *


class TestBinarySearch(unittest.TestCase):
    def test_should_find(self):
        # given
        testlist = [3, 5, 9, 12, 13, 19]
        target = 5
        expected = 1

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(binary_search, testlist, target)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")

    def test_should_not_find(self):
        # given
        testlist = [3, 5, 9, 12, 13, 19]
        target = 18
        expected = -1

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(binary_search, testlist, target)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")

if __name__ == '__main__':
    unittest.main()
