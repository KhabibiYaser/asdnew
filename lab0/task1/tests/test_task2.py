import unittest
from lab0.task1.src.task2 import sum_with_square

class TestTask2(unittest.TestCase):
    def test_valid_numbers(self):
        self.assertEqual(sum_with_square(12, 5), 37)

    def test_out_of_range(self):
        with self.assertRaises(ValueError):
            sum_with_square(-10**9 - 1, 10**9)

if __name__ == '__main__':
    unittest.main()
