# Лабораторная работа №0: `Введение в алгоритмы`

Студент ИТМО, Хабиби Ясер, вариант 23

### Навигация

- [ ] [Задача 1 - Сложение чисел](task1/)
- [ ] [Задача 2 - Числа Фибоначчи](task2/)
- [ ] [Задача 3 - Последняя цифра числа Фибоначчи](task3/)

## Описание

Лабораторная работа посвящена введению в алгоритмы. В рамках лабораторной работы были изучены и реализованы:
- Основные методы работы с числами и массивами.
- Применение рекурсии на примере чисел Фибоначчи.
- Организация ввода и вывода данных через файлы.
- Оптимизация вычислений для работы с большими числами.

## Запуск проекта

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/your-repo/lab0.git

Перейдите в папку с проектом:
```bash
cd lab0

#Запуск всех задач:
for script in lab0/*/src/*.py; do PYTHONPATH=$(pwd) python3 "$script"; done

#Запуск всех тестов задач:
for script in lab0/*/tests/*.py; do PYTHONPATH=$(pwd) python3 "$script"; done
