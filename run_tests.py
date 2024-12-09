import os
import subprocess


EXCLUDE_DIRS = {'.git','.idea', 'myenv', 'venv', '__pycache__','lab0'}

# Функция для запуска тестов
def run_tests(test_file):
    try:
        print(f"Запуск тестов: {test_file}")
        # Запуск тестов через unittest
        subprocess.run(['python3', test_file], check=True)
        print("------ Тесты выполнены успешно! -------")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при запуске тестов: {e}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")


# Функция для поиска и запуска тестов в каждой лабораторной работе
def run_all_tests(base_path):
    """Запуск всех тестов в лабораторных работах."""
    for lab_folder in os.listdir(base_path):
        lab_path = os.path.join(base_path, lab_folder)

        if os.path.isdir(lab_path) and lab_folder not in EXCLUDE_DIRS:
            print(f"\n---------- запуск лабораторной работы: {lab_folder} ------------")

            test_folder = os.path.join(lab_path, 'task6', 'tests')  # Путь к папке с тестами
            test_file = os.path.join(test_folder, 'tests.py')  # Путь к тестам

            # Проверка, существует ли папка с тестами и файл tests.py
            print(f"Проверка пути к тестам: {test_file}")
            if os.path.isfile(test_file):
                run_tests(test_file)
            else:
                print(f"Папка с тестами не найдена для лабораторной работы {lab_path}.")


# Главная функция
def main():
    base_path = '/Users/yasirkhabibi/Desktop/asdnew'  # Путь к директории с лабораторными работами
    run_all_tests(base_path)


if __name__ == '__main__':
    main()
