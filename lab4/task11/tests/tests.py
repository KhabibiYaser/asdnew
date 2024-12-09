import unittest
from lab4.task11.src.bureaucracy_queue import process_queue

class TestBureaucracyQueue(unittest.TestCase):
    def test_example_cases(self):
        # given
        n1, m1, demands1 = 3, 2, [1, 2, 3]
        n2, m2, demands2 = 4, 5, [2, 5, 2, 3]

        # when
        result1 = process_queue(n1, m1, demands1)
        result2 = process_queue(n2, m2, demands2)

        # then
        self.assertEqual(result1, ["2", "3 1"])  # Пример 1
        self.assertEqual(result2, ["3", "4 1 2"])  # Пример 2

    def test_no_people_left(self):
        # given
        n, m, demands = 2, 10, [1, 1]

        # when
        result = process_queue(n, m, demands)

        # then
        self.assertEqual(result, ["-1"])  # Все справки выданы, очередь пуста.

    def test_partial_completion(self):
        # given
        n, m, demands = 4, 3, [1, 1, 1, 1]

        # when
        result = process_queue(n, m, demands)

        # then
        self.assertEqual(result, ["1", "1"])  # Остаётся только 1 посетитель.

    def test_large_demand(self):
        # given
        n, m, demands = 5, 5, [5, 5, 5, 5, 5]

        # when
        result = process_queue(n, m, demands)

        # then
        self.assertEqual(result, ["5", "4 4 4 4 4"])  # Все остаются, но с уменьшенным требованием.

    def test_edge_case_no_demands(self):
        # given
        n, m, demands = 3, 10, [0, 0, 0]

        # when
        result = process_queue(n, m, demands)

        # then
        self.assertEqual(result, ["-1"])  # Никто ничего не требует, очередь пуста.

    def test_one_person(self):
        # given
        n, m, demands = 1, 1, [10]

        # when
        result = process_queue(n, m, demands)

        # then
        self.assertEqual(result, ["1", "9"])  # Один человек остаётся с уменьшенным требованием.


if __name__ == '__main__':
    unittest.main()

