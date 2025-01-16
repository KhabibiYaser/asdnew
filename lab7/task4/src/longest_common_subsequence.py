from lab7.utils import measure_performance, file_write, file_read

import os, sys
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)


def lcs_length(seq1, seq2):
    """
    Вычисление длины наибольшей общей подпоследовательности.
    """
    n, m = len(seq1), len(seq2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


def lcs_main(seq1=None, seq2=None):
    """
    Главная функция. Если входные последовательности переданы, используется для тестов.
    Иначе данные читаются из файлов.
    """
    if seq1 is None or seq2 is None:  # Проверяем, переданы ли данные для тестирования
        data = file_read()  # Читаем данные через file_read
        n, seq1 = data[0][0], data[1]  # Первая строка: длина и последовательность 1
        m, seq2 = data[2][0], data[3]  # Вторая строка: длина и последовательность 2

        result = lcs_length(seq1, seq2)  # Вычисляем LCS
        file_write([result])  # Записываем результат
    else:
        result = lcs_length(seq1, seq2)  # Возвращаем результат для тестов
    return result


if __name__ == '__main__':
    measure_performance(lcs_main)
