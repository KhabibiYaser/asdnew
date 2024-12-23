import os
import subprocess

# Исключаемые папки
EXCLUDE_DIRS = {'.idea', 'myenv', 'venv', '__pycache__', 'lab0', '.git'}


def run_all_tests(base_path):
    # Проходим по всем папкам в base_path и сортируем их по имени
    lab_folders = sorted(
        [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f)) and f not in EXCLUDE_DIRS]
    )

    # Проходим по каждой лабораторной работе
    for lab_folder in lab_folders:
        lab_path = os.path.join(base_path, lab_folder)
        print(f"---------- запуск тестов: {lab_folder} ------------")

        # Ищем задачи внутри папки лабораторной работы
        task_folders = sorted(
            [f for f in os.listdir(lab_path) if os.path.isdir(os.path.join(lab_path, f)) and f not in EXCLUDE_DIRS]
        )

        tests_found = False
        for task_folder in task_folders:
            task_path = os.path.join(lab_path, task_folder)
            tests_folder = os.path.join(task_path, 'tests')
            test_file = os.path.join(tests_folder, 'tests.py')

            # Проверяем наличие тестового файла
            if not os.path.isfile(test_file):
                continue

            tests_found = True
            print(f"Запуск тестов: {test_file}")
            try:
                subprocess.run(['python3', '-m', 'unittest', test_file], check=True, text=True)
            except subprocess.CalledProcessError:
                print(f"ОШИБКА: Тесты завершились неудачей в {test_file}")

        if tests_found:
            print(f"{lab_folder.upper()}: ТЕСТЫ УСПЕШНО ВЫПОЛНЕНЫ\n")
        else:
            print(f"{lab_folder.upper()}: ТЕСТЫ НЕ НАЙДЕНЫ\n")


# Основная часть
if __name__ == "__main__":
    base_path = '~/Desktop/asdnew'  # Путь к проекту
    run_all_tests(os.path.expanduser(base_path))




# import os,sys
# import subprocess
#
#
# EXCLUDE_DIRS = {'.git','.idea', 'myenv', 'venv', '__pycache__','lab0'}
#
# # Функция для запуска тестов
# def run_tests(test_file):
#     try:
#         print(f"Запуск тестов: {test_file}")
#         # Запуск тестов через unittest
#         subprocess.run(['python3', test_file], check=True)
#         print("------ Тесты выполнены успешно! -------")
#     except subprocess.CalledProcessError as e:
#         print(f"Ошибка при запуске тестов: {e}")
#     except Exception as e:
#         print(f"Неизвестная ошибка: {e}")
#
#
# # Функция для поиска и запуска тестов в каждой лабораторной работе
# def run_all_tests(base_path):
#     """Запуск всех тестов в лабораторных работах."""
#     for lab_folder in os.listdir(base_path):
#         lab_path = os.path.join(base_path, lab_folder)
#
#         if os.path.isdir(lab_path) and lab_folder not in EXCLUDE_DIRS:
#             print(f"\n---------- запуск лабораторной работы: {lab_folder} ------------")
#
#             test_folder = os.path.join(lab_path, 'task6', 'tests')  # Путь к папке с тестами
#             test_file = os.path.join(test_folder, 'tests.py')  # Путь к тестам
#
#             # Проверка, существует ли папка с тестами и файл tests.py
#             print(f"Проверка пути к тестам: {test_file}")
#             if os.path.isfile(test_file):
#                 run_tests(test_file)
#             else:
#                 print(f"Папка с тестами не найдена для лабораторной работы {lab_path}.")
#
#
# # Главная функция
# def main():
#     base_path = '/Users/yasirkhabibi/Desktop/asdnew'  # Путь к директории с лабораторными работами
#     run_all_tests(base_path)
#
#
# if __name__ == '__main__':
#     main()