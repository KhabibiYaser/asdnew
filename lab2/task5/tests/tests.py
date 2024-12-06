# -*- coding: utf-8 -*-
import unittest
import random
from collections import Counter

from lab2.task5.src.majority_delegate import *


# helper
def answer(testlist):
    return Counter(testlist).most_common(1)[0][1] > len(testlist) // 2 if testlist else 0 # Это точное решение, как сравнение с гарантированно верным ответом


class TestMajorityDelegate(unittest.TestCase):
    def test_should_no_majority(self):
        # given
        testlist = [1, 2, 3, 1, 2]
        expected = answer(testlist)

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(majority_delegate, testlist)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")

    def test_should_empty(self): # тест на пустой списко
        # given
        testlist = []
        expected = answer(testlist)

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(majority_delegate, testlist)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")

    def test_should_majority(self): # тест где большинство есть
        # given
        testlist = [4, 2, 3, 4, 4, 1, 4]
        expected = answer(testlist)

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(majority_delegate, testlist)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")

    def test_should_random(self):
        # given
        testlist = [random.randint(-10 ** 9, 10 ** 9) for _ in range(random.randint(1, 20000))]
        expected = answer(testlist)

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(majority_delegate, testlist)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")

    def test_should_random_majority(self):
        # given
        testlist = [random.randint(-10 ** 9, 10 ** 9) for _ in range(1000)]
        testlist += [random.randint(-10 ** 9, 10 ** 9)] * 2000
        expected = answer(testlist)

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(majority_delegate, testlist)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")


if __name__ == '__main__':
    unittest.main()
