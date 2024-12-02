import os
import subprocess

# Исключаемые папки
EXCLUDE_DIRS = {'.idea', 'myenv', 'venv', '__pycache__','lab0'}

# Функция для запуска всех .py файлов в src
def run_all_python_scripts(base_path):
    # Проходим по всем папкам в base_path и сортируем их по имени
    lab_folders = sorted(
        [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f)) and f not in EXCLUDE_DIRS])

    # Проходим по каждой лабораторной работе
    for lab_folder in lab_folders:
        lab_path = os.path.join(base_path, lab_folder)
        print(f"---------- запуск лабораторной работы: {lab_folder} ------------")

        # Получаем список задач в лабораторной работе и сортируем их
        task_folders = sorted(
            [f for f in os.listdir(lab_path) if os.path.isdir(os.path.join(lab_path, f)) and f not in EXCLUDE_DIRS])
        # Проходим по каждой задаче
        for task_folder in task_folders:
            task_path = os.path.join(lab_path, task_folder)
            src_folder = os.path.join(task_path, 'src')
            # Проверяем, есть ли Python-скрипты в папке src
            python_files = [f for f in os.listdir(src_folder) if f.endswith('.py')]
            for python_file in python_files:
                script_path = os.path.join(src_folder, python_file)
                print(f"---------------  задача : {task_folder} -------------")
                print(f"Запуск: {script_path}")

                # Запускаем скрипт
                try:
                    subprocess.run(['python3', script_path], check=True)
                    print("------ Выполнена Успешно ! -------\n")
                except subprocess.CalledProcessError:
                    print("------ Ошибка при выполнении скрипта! -------\n")


# Основная часть
if __name__ == "__main__":
    base_path = '~/Desktop/asdnew/newlabs'  # Путь к проекту
    run_all_python_scripts(os.path.expanduser(base_path))


