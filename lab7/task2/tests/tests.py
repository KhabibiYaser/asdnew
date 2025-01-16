import unittest
from lab7.task2.src.primitive_calculator import optimal_sequence
from lab7.utils import measure_performance

class TestPrimitiveCalculator(unittest.TestCase):

    def test_example_case_1(self):
        # given
        n = 1

        # when
        result, elapsed_time, peak_memory = measure_performance(optimal_sequence, n)

        # then
        self.assertEqual(result, (0, [1]))
        self.assertLessEqual(elapsed_time, 1, "Execution time exceeded 1 second")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")

    def test_example_case_2(self):
        # given
        n = 5

        # when
        result, elapsed_time, peak_memory = measure_performance(optimal_sequence, n)

        # then
        self.assertEqual(result, (3, [1, 2, 4, 5]))
        self.assertLessEqual(elapsed_time, 1, "Execution time exceeded 1 second")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")

    def test_large_input(self):
        # given
        n = 96234

        # when
        result, elapsed_time, peak_memory = measure_performance(optimal_sequence, n)

        # then
        self.assertGreater(len(result[1]), 0, "Sequence should not be empty")
        self.assertLessEqual(elapsed_time, 1, "Execution time exceeded 1 second")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")

if __name__ == '__main__':
    unittest.main()

