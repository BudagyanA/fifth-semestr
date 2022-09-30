from typing import List
from mathstats import MathStats # mathstats.py - файл с классом с формулами
import numpy as np
import matplotlib.pyplot as plt

FILE = 'Retail.csv'
FILE2 = 'MarketingSpend.csv'


def main():
    # запускающая функция
    data = read_data(FILE)
    c = count_invoice(data[:5])
    print(f'Всего инвойсов (invoices): {c}')  # 2
    c = count_invoice(data[:11])
    print(f'Всего инвойсов (invoices): {c}')  # 5
    c = count_invoice(data)
    print(f'Всего инвойсов (invoices): {c}')  # 16522
    
    stock_code = 21730
    print(f'Количество записей с кодом {stock_code}: ', get_total_quantity(data, stock_code))
  
    data2 = MathStats(FILE2)

    print("Среднее: ", data2.get_mean)
    print("Максимум: ", data2.max)
    print("Минимум: ", data2.min)
    print("Дисперсия: ", data2.disp)
    print("Среднее квадратичное отклонение: ", data2.sigma_sq)

    print(marketing_plot(data2.data))
    print(retail_plot(data))
    


def read_data(file: str) -> List[dict]:
    # считывание данных и возвращение значений в виде списка из словарей
    import csv
    data = []
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for _r in reader:
            row = {
                'InvoiceNo': _r['InvoiceNo'],
                'InvoiceDate': _r['InvoiceDate'],
                'StockCode': int(_r['StockCode']),
                'Quantity': int(_r['Quantity'])
            }
            data.append(row)
    return data


def count_invoice(data: List[dict]) -> int:
    count = 0
    # 1. Создаем список виденных инвойсов (пустой), пробегаемся по
    # data и если в списке нет очередного инвойса, то добавляем его туда
    # в конце считаем сколько элементов в нем есть.

    # 2. Создаем множество и добавляем туда по очереди все встреченные
    # элементы. Поскольку это множество, инвойсы в нем не будут
    # повторяться. В конце считаем сколько элементов.

    # 3. Counter
    from collections import Counter

    # Реализуем получение номер invoices и помещение их в список
    # Переписано через генератор списка
    invoices = [_el['InvoiceNo'] for _el in data]

    count = len(Counter(invoices))
    return count


def count_different_values(data: List[dict], key: str) -> int:
    """
    Функция должна возвращать число различных значений для столбца key в списке data

    key - InvoiceNo или InvoiceDate или StockCode
    """
    value_set = set() 
    for i in data:
        value_set.add(i[key]) 
  
    result = len(value_set) 
    return result


def get_total_quantity(data: List[dict], stock_code: int) -> int:
    """
    Возвращает общее количество проданнорго товара для данного stock_code
    """
    result = 0
    
    for i in data:
        
        if i['StockCode'] == stock_code: 
            result += 1
    
    return result


def marketing_plot(data):

    
    sums_online = np.zeros(12)
    sums_offline = np.zeros(12)
    
    months = np.arange(1, 13, 1)

    
    for i in data:
        
        month = int(i['Date'][5:7])  

        
        sums_online[month-1] += i['Online']
        sums_offline[month-1] += i['Offline']

    
    plt.barh(months, sums_online, label='Online')
    
    plt.barh(months, sums_offline, left=sums_online, label='Offline')

    
    plt.xticks(np.arange(0, 250000, 20000), rotation=45)
    plt.yticks(months, ['Янв', 'Фев', 'Март', 'Апр', 'Май', 'Июнь', 'Июль', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек'])
    
    
    for onl, month, off in zip(sums_online, months, sums_offline):
        
        plt.text(onl / 3, month, round(onl, 2))

        plt.text(onl + (off / 3), month, round(off, 2))

        
        plt.text(onl + off, month, round(onl + off, 2))

    plt.legend(loc=7)

    plt.xlabel('Продажи')
    plt.ylabel('Месяцы')
  
    plt.show()


def retail_plot(data):

    quantities = {
        '01': np.zeros((31,), dtype=int),
        '02': np.zeros((28,), dtype=int),
        '03': np.zeros((31,), dtype=int),
        '04': np.zeros((30,), dtype=int),
        '05': np.zeros((31,), dtype=int),
        '06': np.zeros((30,), dtype=int),
        '07': np.zeros((31,), dtype=int),
        '08': np.zeros((31,), dtype=int),
        '09': np.zeros((30,), dtype=int),
        '10': np.zeros((31,), dtype=int),
        '11': np.zeros((30,), dtype=int),
        '12': np.zeros((31,), dtype=int)
    }


    for i in data:
        month = str(i['InvoiceDate'][5:7])
        day = int(i['InvoiceDate'][8:])
        quantities[month][day-1] += i['Quantity']

    quantities = np.concatenate(list(quantities.values()))
    quantities = [np.nan if i == 0 else i for i in quantities]

    x_arr = np.arange(1, 366, dtype=int)

    plt.xlabel('Дни')
    plt.ylabel('Количество продаж')

    plt.scatter(x_arr, quantities)
    plt.show()
    

if __name__ == "__main__":
    main() 