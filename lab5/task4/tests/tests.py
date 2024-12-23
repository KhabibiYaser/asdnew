import unittest
from lab5.task4.src.build_heap import build_heap
from lab5.utils import measure_performance


class TestBuildHeap(unittest.TestCase):
    def test_example_1(self):
        # given
        array = [5, 4, 3, 2, 1]
        expected_swaps = [(1, 4), (0, 1), (1, 3)]

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(build_heap, array)

        # then
        self.assertEqual(result, expected_swaps)
        self.assertLessEqual(elapsed_time, 3, "Execution time exceeded 3 seconds")
        self.assertLessEqual(peak_memory_megabytes, 512, "Memory usage exceeded 512 MB")

    def test_example_2(self):
        # given
        array = [1, 2, 3, 4, 5]
        expected_swaps = []

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(build_heap, array)

        # then
        self.assertEqual(result, expected_swaps)
        self.assertLessEqual(elapsed_time, 3, "Execution time exceeded 3 seconds")
        self.assertLessEqual(peak_memory_megabytes, 512, "Memory usage exceeded 512 MB")

    def test_large_input(self):
        # given
        array = list(range(1000, 0, -1))
        # Проверка только на корректное выполнение, без конкретного результата

        # when
        result, elapsed_time, peak_memory_megabytes = measure_performance(build_heap, array)

        # then
        self.assertLessEqual(elapsed_time, 3, "Execution time exceeded 3 seconds")
        self.assertLessEqual(peak_memory_megabytes, 512, "Memory usage exceeded 512 MB")


if __name__ == "__main__":
    unittest.main()
