# -*- coding: utf-8 -*-

import unittest
import random

from lab2.task1.src.merge_sort import *


class TestMergeSort(unittest.TestCase):
    def check_sort(self, testlist): # используется во всех тестах , чек производительности
        result, elapsed_time, peak_memory_megabytes = measure_performance(merge_sort, testlist)
        self.assertEqual(result, sorted(testlist))

    def test_should_empty(self):
        testlist = [] # пустой лист
        self.check_sort(testlist)

    def test_should_random(self):
        testlist = [random.randint(-10 ** 9, 10 ** 9) for _ in range(random.randint(1, 20000))]
        self.check_sort(testlist)   # случ кол-во элементов случ размера

    def test_should_max_size(self):
        testlist = [random.randint(-10 ** 9, 10 ** 9) for _ in range(20000)]
        self.check_sort(testlist) # макс кол-во элементов случ размера

    def test_should_max_size_reverse_sorted(self):
        testlist = [random.randint(-10 ** 9, 10 ** 9) for _ in range(20000)]
        testlist.sort(reverse=True)
        self.check_sort(testlist) # макс кол-во элементов случ размера , но в обратном порядке

    def test_should_huge_numbers(self):
        testlist = [1000000000, 999999999, 999999998]
        self.check_sort(testlist) # отдельная проверка макс

    def test_should_not_list(self):
        self.assertRaises(TypeError, merge_sort, 2) # если передадим не список (typeError)


if __name__ == '__main__':
    unittest.main()
