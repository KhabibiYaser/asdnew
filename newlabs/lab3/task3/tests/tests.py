import unittest
from lab3.task3.src.scarecrow_sort import *
from lab3.utils import *


class TestScarecrowSort(unittest.TestCase):
    def check_sorting(self, filename, answer):
        n, k, array = file_read_int_int_array(filename)
        result, elapsed_time, peak_memory_megabytes = measure_performance(can_sort_dolls, n, k, array)
        self.assertEqual(result, answer)


    def test_example_a(self):
        self.check_sorting('../txtf/test_input1.txt', "NO")


    def test_example_b(self):
        self.check_sorting('../txtf/test_input2.txt', "YES")


    def test_example_c(self):
        self.check_sorting('../txtf/test_input3.txt', "NO")


if __name__ == '__main__':
    unittest.main()
