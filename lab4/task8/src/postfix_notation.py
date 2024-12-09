from lab4.utils import file_read, file_write, measure_performance
import os

def evaluate_postfix(expression):
    stack = []
    operators = {'+', '-', '*'}

    for token in expression:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):  # Если это число
            stack.append(int(token))
        elif token in operators:  # Если это оператор
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            stack.append(result)


    return stack.pop()


def process_postfix():
    data = file_read()
    n = int(data[0])
    expression = data[1].split()

    result = evaluate_postfix(expression)
    file_write([result])

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    measure_performance(process_postfix)
