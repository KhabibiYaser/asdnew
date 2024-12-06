# -*- coding: utf-8 -*-

import unittest

# Загружаем все тесты из файлов test_task1.py, test_task2.py, test_task3.py, test_task4.py
test_loader = unittest.TestLoader()
test_suite = unittest.TestSuite()

# Указываем пути к тестовым файлам
test_files = [
    "lab0.task1.tests.test_task1",
    "lab0.task1.tests.test_task2",
    "lab0.task1.tests.test_task3",
    "lab0.task1.tests.test_task4",
]

# Добавляем все тесты из указанных файлов
for test_file in test_files:
    test_suite.addTests(test_loader.loadTestsFromName(test_file))

# Запускаем тесты
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)
