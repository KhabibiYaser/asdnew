import unittest
from lab6.task3.src.hash_chains import process_hash_table
from lab6.utils import measure_performance

class TestHashChains(unittest.TestCase):



    def test_add_find_and_delete(self):
        # given
        input_data = [
            "3",  # Количество сегментов
            "add hello",
            "add world",
            "find hello",
            "find world",
            "del hello",
            "find hello"
        ]
        expected = ["yes", "yes", "no"]

        # when
        result, elapsed_time, peak_memory = measure_performance(process_hash_table, input_data)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 7, "Execution time exceeded 7 seconds")
        self.assertLessEqual(peak_memory, 512, "Memory usage exceeded 512 MB")

    def test_multiple_operations(self):
        # given
        input_data = [
            "4",  # Количество сегментов
            "add test",
            "add test",
            "find test",
            "del test",
            "find test",
            "check 1"
        ]
        expected = ["yes", "no", ""]

        # when
        result, elapsed_time, peak_memory = measure_performance(process_hash_table, input_data)

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(elapsed_time, 7, "Execution time exceeded 7 seconds")
        self.assertLessEqual(peak_memory, 512, "Memory usage exceeded 512 MB")

if __name__ == "__main__":
    unittest.main()
