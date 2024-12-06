import unittest

from lab2.task6.src.max_profit_search import *


class TestMaxProfit(unittest.TestCase):
    def test_should_example_a(self):
        # given
        testfile = '../txtf/test_input1.txt'
        expected = 46

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(max_profit_search_main, testfile)

        # then
        self.assertEqual(result, expected)
        # self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        # self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")
        # Performance check wasn't requested in the task.


    def test_should_example_b(self):
        # given
        testfile = '../txtf/test_input2.txt'
        expected = 56

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(max_profit_search_main, testfile)

        # then
        self.assertEqual(result, expected)
        # self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        # self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")
        # Performance check wasn't requested in the task.


    def test_should_example_c(self):
        # given
        testfile = '../txtf/test_input3.txt'
        expected = 14

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(max_profit_search_main, testfile)

        # then
        self.assertEqual(result, expected)
        # self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        # self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")
        # Performance check wasn't requested in the task.

if __name__ == '__main__':
    unittest.main()
