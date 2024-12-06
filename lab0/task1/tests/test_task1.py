import unittest
from lab0.task1.src.task1 import sum_of_nums

class TestTask1(unittest.TestCase):
    def test_valid_numbers(self):
        self.assertEqual(sum_of_nums(12, 25), 37)

    def test_out_of_range(self):
        with self.assertRaises(ValueError):
            sum_of_nums(-10**9 - 1, 10**9)

if __name__ == '__main__':
    unittest.main()
