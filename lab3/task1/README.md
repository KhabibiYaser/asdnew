 # Задача 1: `Улучшение Quick Sort`
 
 ## Задание
 
 Быстрая сортировка была улучшена путём выбора случайного pivot-элемента и деления массива на три части. Программа анализирует эффективность алгоритма и проверяет его производительность.
 
 ## Input / Output
 
 | Input           | Output                                   |
 | --------------- | ---------------------------------------- |
 | `5`             | `1 2 3 4 5`                             |
 | `5 4 3 2 1`     |                                          |
 
 ## Ограничения

$$
( 1 \leq n \leq 100,000 )
$$
$$
( |a_i| \leq 10^9 )
$$ 
 ## Запуск задачи
 
 ```bash
 for script in lab3/*/src/*.py; do PYTHONPATH=$(pwd) python3 "$script"; done
 ```
 
 ## Тестирование
 
 ```bash
 PYTHONPATH=. python3 lab3/task1/tests/tests.py
 ```
 