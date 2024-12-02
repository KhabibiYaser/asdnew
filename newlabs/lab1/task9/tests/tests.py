import unittest
from lab1.task9.src.task9 import binary_addition, binary_addition_main
from lab1.utils import file_write

class TestTask9(unittest.TestCase):
    def test_binary_addition(self):
        # Пример из задачи
        a = [1, 0, 1, 1]
        b = [1, 1, 0, 1]
        result = binary_addition(a, b)
        self.assertEqual(result, [1, 1, 0, 0, 0])

        # Другие тесты
        self.assertEqual(binary_addition([0, 0, 1], [1, 1, 1]), [1, 0, 0, 0])
        self.assertEqual(binary_addition([1, 1, 1], [1, 1, 1]), [1, 1, 1, 0])

    def test_file_processing(self):
        # Пишем корректные тестовые данные в input.txt
        with open('../txtf/input.txt', 'w') as file:
            file.write("1011\n")  # Первое число
            file.write("1101\n")  # Второе число

        # Вызываем основную функцию
        binary_addition_main()

        # Проверяем результат в output.txt
        with open('../txtf/output.txt', 'r') as file:
            result = file.read().strip()
        self.assertEqual(result, "1 1 0 0 0")  # Ожидаемый результат

if __name__ == '__main__':
    unittest.main()
