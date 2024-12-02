import unittest
from itertools import accumulate

from lab2.task6.src.max_profit_search import *

class TestMaxProfit(unittest.TestCase):

    def get_optimal_price(self, input_file_path):
        name, prices = file_read_company_data(input_file_path)
        prices = [price for date, price in prices]
        profit_array = [prices[i] - prices[i - 1] for i in range(1, len(prices))]

        result, elapsed_time, peak_memory_megabytes = measure_performance(max_profit_search_main, input_file_path)
        self.assertEqual(result, max(accumulate(profit_array, lambda x, y: max(y, x + y))))

    def test_example_a(self):
        self.get_optimal_price('../txtf/test_input1.txt')


    def test_example_b(self):
        self.get_optimal_price('../txtf/test_input2.txt')


    def test_example_c(self):
        self.get_optimal_price('../txtf/test_input3.txt')

if __name__ == '__main__':
    unittest.main()
