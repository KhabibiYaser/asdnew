import unittest
from lab4.task8.src.postfix_notation import evaluate_postfix

class TestPostfixNotation(unittest.TestCase):
    def test_simple_expression(self):
        # given
        expression = ["8", "9", "+", "1", "7", "-", "*"]

        # when
        result = evaluate_postfix(expression)

        # then
        self.assertEqual(result, -102)

    def test_single_number(self):
        # given
        expression = ["5"]

        # when
        result = evaluate_postfix(expression)

        # then
        self.assertEqual(result, 5)

    def test_multiple_operations(self):
        # given
        expression = ["2", "3", "*", "5", "+"]

        # when
        result = evaluate_postfix(expression)

        # then
        self.assertEqual(result, 11)

    def test_large_expression(self):
        # given
        expression = ["10", "5", "*", "2", "3", "+", "-"]

        # when
        result = evaluate_postfix(expression)

        # then
        self.assertEqual(result, 45)


if __name__ == '__main__':
    unittest.main()
