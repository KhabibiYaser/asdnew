import unittest
from lab4.task1.src.stack import Stack, process_stack_commands
from lab4.utils import file_read, file_write


class TestStack(unittest.TestCase):
    def test_stack_operations(self):
        # given
        stack = Stack()
        stack.push(10)
        stack.push(20)

        # when
        result1 = stack.pop()
        result2 = stack.pop()

        # then
        self.assertEqual(result1, 20)
        self.assertEqual(result2, 10)

    def test_process_stack_commands(self):
        # given
        input_data = [
            "6",
            "+ 10",
            "+ 20",
            "-",
            "+ 30",
            "-",
            "-"
        ]
        expected_output = [20, 30, 10]

        with open('../txtf/input.txt', 'w') as f:
            f.write("\n".join(input_data))

        # when
        process_stack_commands()

        # then
        with open('../txtf/output.txt', 'r') as f:
            output = list(map(int, f.read().strip().split("\n")))

        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
