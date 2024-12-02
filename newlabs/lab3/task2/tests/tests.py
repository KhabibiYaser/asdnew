import unittest
from lab3.task2.src.anti_qsort import *
from lab3.utils import *


class TestAntiQSort(unittest.TestCase):
    def check_antiqsorting(self, number, testlist):
        result, elapsed_time, peak_memory_megabytes = measure_performance(anti_qsort, number)
        self.assertEqual(result, testlist)


    def test_should_antiqsort_small(self):
        number = 3
        testlist = [1, 3, 2]
        self.check_antiqsorting(number, testlist)


    def test_should_antiqsort_big(self):
        number = 10
        testlist = [1, 4, 6, 8, 10, 5, 3, 7, 2, 9]
        self.check_antiqsorting(number, testlist)


if __name__ == '__main__':
    unittest.main()
