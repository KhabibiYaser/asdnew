# -*- coding: utf-8 -*-

import unittest
import random
from collections import Counter
from lab2.task5.src.majority_delegate import *


class TestMajorityDelegate(unittest.TestCase):

    def check_majority(self, testlist):
        result, elapsed_time, peak_memory_megabytes = measure_performance(majority_delegate, testlist)
        self.assertEqual(result, Counter(testlist).most_common(1)[0][1] > len(testlist) // 2 if testlist else 0) # Это точное решение, как сравнение с гарантированно верным ответом

    def test_should_no_majority(self):
        testlist = [1, 2, 3, 1, 2]
        self.check_majority(testlist)


    def test_should_empty(self):
        testlist = []
        self.check_majority(testlist) # тест на пустой списко


    def test_should_majority(self):
        testlist = [4, 2, 3, 4, 4, 1, 4]
        self.check_majority(testlist) # тест где большинство есть


    def test_should_random(self):
        testlist = [random.randint(-10 ** 9, 10 ** 9) for _ in range(random.randint(1, 20000))]
        self.check_majority(testlist)


    def test_should_random_majority(self):
        testlist = [random.randint(-10 ** 9, 10 ** 9) for _ in range(1000)]
        testlist += [random.randint(-10 ** 9, 10 ** 9)] * 2000
        self.check_majority(testlist)


if __name__ == '__main__':
    unittest.main()
