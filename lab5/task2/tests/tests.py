import unittest
from lab5.task2.src.tree_height import *
from lab5.utils import *


import os , sys
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)

class TestTreeHeight(unittest.TestCase):
    def test_simple_tree(self):
        # given
        n = 5
        parents = [-1, 0, 0, 1, 1]
        expected = 3

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(calculate_tree_height, n, parents)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")

    def test_single_node(self):
        # given
        n = 1
        parents = [-1]
        expected = 1

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(calculate_tree_height, n, parents)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")

    def test_linear_tree(self):
        # given
        n = 4
        parents = [-1, 0, 1, 2]
        expected = 4

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(calculate_tree_height, n, parents)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")

    def test_balanced_tree(self):
        # given
        n = 7
        parents = [-1, 0, 0, 1, 1, 2, 2]
        expected = 3

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(calculate_tree_height, n, parents)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory_megabytes, 256, "Memory usage exceeded 256 MB")

if __name__ == "__main__":
    unittest.main()