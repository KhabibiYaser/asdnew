import unittest
import random
from lab7.task4.src.longest_common_subsequence import lcs_main


class TestLongestCommonSubsequence(unittest.TestCase):
    def test_basic_case(self):
        # given
        input_data = ([2, 7, 5], [2, 5])
        expected_output = 2

        # when
        result = lcs_main(*input_data)

        # then
        self.assertEqual(result, expected_output)

    def test_full_match(self):
        # given
        input_data = ([1, 2, 3, 4], [1, 2, 3, 4])
        expected_output = 4

        # when
        result = lcs_main(*input_data)

        # then
        self.assertEqual(result, expected_output)

    def test_large_input(self):
        # given
        input_data = (
            [random.randint(1, 100) for _ in range(100)],
            [random.randint(1, 100) for _ in range(100)],
        )

        # when
        result = lcs_main(*input_data)

        # then
        self.assertTrue(isinstance(result, int))  # Проверяем, что результат целое число

    def test_no_common_subsequence(self):
        # given
        input_data = ([7], [1])
        expected_output = 0

        # when
        result = lcs_main(*input_data)

        # then
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
