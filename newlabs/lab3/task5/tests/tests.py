import unittest
from lab3.task5.src.hirsh_index import *
from lab3.utils import *


class TestHirshIndex(unittest.TestCase):
    def check_hirsh_index(self, filename, expected):
        line = file_read_array(filename)
        result, elapsed_time, peak_memory_megabytes = measure_performance(hirsh_index, line)
        self.assertEqual(result, expected)


    def test_example_a(self):
        self.check_hirsh_index('../txtf/test_input1.txt', 0)


    def test_example_b(self):
        self.check_hirsh_index('../txtf/test_input2.txt', 1)


    def test_example_c(self):
        self.check_hirsh_index('../txtf/test_input3.txt', 3)


if __name__ == '__main__':
    unittest.main()
