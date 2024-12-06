import unittest
from  lab0.task1.src.task3 import sum_from_file
from lab0.utils import file_write

class TestTask3(unittest.TestCase):
    def test_file_processing(self):
        file_write([12, 25], '../txtf/input.txt')
        sum_from_file()
        with open('../txtf/output.txt', 'r') as file:
            result = file.read().strip()
        self.assertEqual(result, "37")

if __name__ == '__main__':
    unittest.main()
