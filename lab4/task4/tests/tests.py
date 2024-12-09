import unittest
from lab4.task4.src.brackets_checker import check_brackets

class TestBracketsChecker(unittest.TestCase):
    def test_success_cases(self):
        # given
        cases = [
            ("[]", "Success"),
            ("{}", "Success"),
            ("()", "Success"),
            ("{[()]}", "Success"),
            ("foo(bar);", "Success"),
            ("", "Success")
        ]

        for sequence, expected in cases:
            # when
            result = check_brackets(sequence)

            # then
            self.assertEqual(result, expected)

    def test_error_cases(self):
        # given
        cases = [
            ("{", 1),
            ("}", 1),
            ("{[}", 3),
            ("foo(bar[i);", 10),
            ("(}", 2)
        ]

        for sequence, expected in cases:
            # when
            result = check_brackets(sequence)

            # then
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
