import unittest
from lab4.task1.src.stack import process_stack_commands
from lab4.utils import measure_performance


class TestStack(unittest.TestCase):

    def test_stack_operations(self):
        # given
        commands = [
            "+ 10",
            "+ 20",
            "+ 30",
            "-",
            "-",
            "-",
        ]
        expected = [30, 20, 10]

        # when
        result, elapsed_time, peak_memory = measure_performance(process_stack_commands, commands)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")

    def test_empty_stack(self):
        # given
        commands = ["-"]
        expected = [None]

        # when
        result, elapsed_time, peak_memory = measure_performance(process_stack_commands, commands)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")

    def test_mixed_operations(self):
        # given
        commands = [
            "+ 5",
            "+ 15",
            "-",
            "+ 25",
            "-",
            "-",
        ]
        expected = [15, 25, 5]

        # when
        result, elapsed_time, peak_memory = measure_performance(process_stack_commands, commands)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")


if __name__ == '__main__':
    unittest.main()