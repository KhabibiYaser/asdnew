# -*- coding: utf-8 -*-
import unittest
import random

from lab2.task1.src.merge_sort import *


# helper
def answer(testlist):
    return sorted(testlist)


class TestMergeSort(unittest.TestCase):
    def test_should_empty(self): # пустой лист
        # given
        testlist = []
        expected = answer(testlist)

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(merge_sort, testlist)
        # используется во всех тестах , чек производительности

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")

    def test_should_random(self):   # случ кол-во элементов случ размера
        # given
        testlist = [random.randint(-10 ** 9, 10 ** 9) for _ in range(random.randint(1, 20000))]
        expected = answer(testlist)

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(merge_sort, testlist)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")

    def test_should_max_size(self): # макс кол-во элементов случ размера
        # given
        testlist = [random.randint(-10 ** 9, 10 ** 9) for _ in range(20000)]
        expected = answer(testlist)

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(merge_sort, testlist)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")

    def test_should_max_size_reverse_sorted(self): # макс кол-во элементов случ размера , но в обратном порядке
        # given
        testlist = [random.randint(-10 ** 9, 10 ** 9) for _ in range(20000)]
        testlist.sort(reverse=True)
        expected = answer(testlist)

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(merge_sort, testlist)

        # then
        self.assertEqual(result, expected)

    def test_should_huge_numbers(self): # отдельная проверка макс
        # given
        testlist = [1000000000, 999999999, 999999998]
        expected = answer(testlist)

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(merge_sort, testlist)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")

    def test_should_not_list(self): # если передадим не список (typeError)
        # given
        testdata = 2

        # when
        try:
            merge_sort(testdata)
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
