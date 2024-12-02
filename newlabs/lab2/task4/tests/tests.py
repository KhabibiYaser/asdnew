# -*- coding: utf-8 -*-

import unittest

from lab2.task4.src.binary_search import *

class TestBinarySearch(unittest.TestCase):


    def test_should_find(self):
        testlist = [3, 5, 9, 12, 13, 19]
        target = 5
        result, elapsed_time, peak_memory_megabytes = measure_performance(binary_search, testlist, target)
        self.assertEqual(result, 1)


    def test_should_not_find(self):
        testlist = [3, 5, 9, 12, 13, 19]
        target = 18
        result, elapsed_time, peak_memory_megabytes = measure_performance(binary_search, testlist, target)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()
