# -*- coding: utf-8 -*-
from lab2.task7.src.max_subarray_search_in_linear_time import *

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)
# pythonpath = os.getenv("PYTHONPATH")

def file_read_company_data(input_file_path='../txtf/input.txt'):
    with open(input_file_path, 'r') as file:
        name = file.readline().strip()
        array = file.readlines()[:]  # считаем весь массив строчек
        array = [tuple(line.split()) for line in array] # переводим в массив пар ()
        array = [(date, int(value)) for date, value in array] # 2elm int
    return name, array


def max_profit_search(prices):
    if len(prices) < 2:
        raise ValueError("Array must contain at least 2 elements for buy/sell.")

    prices = [price for date, price in prices]       # цены на данный момент
    profit_array = [prices[i] - prices[i - 1] for i in range(1, len(prices))]  # дата/цена -> разниц цен -> профит
    buy_day, sell_day, max_profit = kadane(profit_array) # Начало подмассива , Конец подмассива и макс
    return buy_day, sell_day, max_profit


def max_profit_search_main(input_file_path='../txtf/input.txt'):
    name, data = file_read_company_data(input_file_path)
    buy_day, sell_day, profit = max_profit_search(data)
    data = [date for date, price in data]
    answer = f"Компания: {name}\nРассматриваемый период: {data[0]}-{data[-1]}\nДень покупки: {data[buy_day]}\nДень продажи: {data[sell_day]}\nМаксимальная прибыль: {profit}"
    print(answer)
    file_write([answer])
    return profit

if __name__ == "__main__":
    max_profit_search_main()