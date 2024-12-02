import unittest
import random

from lab3.task1.src.qsort_plus import *
from lab3.utils import *


class TestScarecrowSort(unittest.TestCase):
    testlist_empty = []
    testlist_basic = [2, 3, 9, 2, 2]
    testlist_random = [random.randint(-10 ** 9, 10 ** 9) for _ in range(10000)]
    testlist_few_different = [random.randint(-10 ** 9, 10 ** 9) for _ in range(20)] * 500


    def check_sorting(self, testlist):
        result, elapsed_time, peak_memory_megabytes = measure_performance(qsort, testlist)
        self.assertEqual(result, sorted(testlist))


    def test_should_sort_empty(self):
        self.check_sorting(self.testlist_empty)


    def test_should_sort_basic(self):
        self.check_sorting(self.testlist_basic)


    def test_should_sort_random(self):
        self.check_sorting(self.testlist_random)


    def test_should_sort_few_different(self):
        self.check_sorting(self.testlist_few_different)


    def test_should_compare(self):
        result, elapsed_time, peak_memory_megabytes = (
            measure_performance(random_quick_sort, self.testlist_few_different))
        result3, elapsed_time3, peak_memory_megabytes3 = (
            measure_performance(random_quick_sort3, self.testlist_few_different))
        self.assertGreater(elapsed_time, elapsed_time3)


if __name__ == '__main__':
    unittest.main()
