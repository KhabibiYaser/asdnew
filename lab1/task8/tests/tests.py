import unittest
from lab1.task8.src.task8 import selection_sort_with_swaps, sort_main
from lab1.utils import file_write

class TestTask8(unittest.TestCase):
    def test_selection_sort_with_swaps(self):
        # Пример из условия
        arr = [3, 1, 4, 2, 2]
        expected_swaps = [
            "Swap elements at indices 1 and 2.",
            "Swap elements at indices 2 and 4.",
            "Swap elements at indices 3 and 5.",
            "No more swaps needed."
        ]
        result = selection_sort_with_swaps(arr)
        self.assertEqual(result, expected_swaps)

    def test_file_processing(self):
        # Пишем корректные тестовые данные в input.txt
        with open('../txtf/input.txt', 'w') as file:
            file.write("5\n")  # Размер массива
            file.write("3 1 4 2 2\n")  # Массив

        # Вызываем основную функцию
        sort_main()

        # Проверяем результат в output.txt
        with open('../txtf/output.txt', 'r') as file:
            result = file.read().strip().split("\n")
        expected_result = [
            "Swap elements at indices 1 and 2.",
            "Swap elements at indices 2 and 4.",
            "Swap elements at indices 3 and 5.",
            "No more swaps needed."
        ]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
