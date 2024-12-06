import unittest

from lab3.task1.src.qsort_plus import *


# helper
def answer(testlist):
    return sorted(testlist)


class TestScarecrowSort(unittest.TestCase):
    def test_should_sort_empty(self):
        # given
        testlist = []

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(qsort, testlist)

        # then
        self.assertEqual(result, answer(testlist))
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")

    def test_should_sort_basic(self):
        # given
        testlist = [2, 3, 9, 2, 2]

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(qsort, testlist)

        # then
        self.assertEqual(result, answer(testlist))
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")

    def test_should_sort_random(self):
        # given
        testlist = [random.randint(-10 ** 9, 10 ** 9) for _ in range(10000)]

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(qsort, testlist)

        # then
        self.assertEqual(result, answer(testlist))
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")

    def test_should_sort_few_different(self):
        # given
        testlist = [random.randint(-10 ** 9, 10 ** 9) for _ in range(20)] * 500

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(random_quick_sort3, testlist)

        # then
        self.assertEqual(result, answer(testlist))
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")

    def test_should_compare_properly(self):
        # given
        testlist = [random.randint(-10 ** 9, 10 ** 9) for _ in range(20)] * 500

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(random_quick_sort, testlist)
        result3, elapsed_time3, peak_memory_megabytes3 = measure_performance(random_quick_sort3, testlist)

        # then
        self.assertGreater(elapsed_time, elapsed_time3)


if __name__ == '__main__':
    unittest.main()
