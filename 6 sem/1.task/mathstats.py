"""
Для вычисления дисперсии и ср. квадр. отклонения использовать 
https://myslide.ru/documents_3/b9d7b50c38e81a4b8b7645742d3b22c7/img10.jpg
"""
from math import sqrt

class MathStats():
    def __init__(self, file):
        import csv

        self._file = file
        self._data = []
        self._mean = None
        self._sum = {'offline': 0, 'online': 0}
        self._max = float('-Inf')
        self._min = float('Inf')
        with open(self._file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for _r in reader:
                row = {
                    'Date': _r[''],
                    'Offline': float(_r['Offline Spend']),
                    'Online': float(_r['Online Spend']),
                }
                self._data.append(row)

    # декоратор property превращает метод в свойство - можно вызывать без скобок
    @property
    def data(self):
        return self._data

    @property
    def get_mean(self):
        """
        Вычисление среднего по оффлайн и онлайн тратам
        """

        for _l in self._data:
            self._sum['offline'] += _l['Offline']
            self._sum['online'] += _l['Online']

        self._mean = (self._sum['offline'] / len(self._data), self._sum['online'] / len(self._data))

        return self._mean

    @property
    def max(self):
        # с помощью генераторов списка выбираем нужные значения в словаре
        # здесь два генератора списка - для Offline и Online
        # затем ищем среди них максимальные значения с помощью функции max
        max_offline = max(i['Offline'] for i in self._data)
        max_online = max(i['Online'] for i in self._data)

        # результат в виде кортежа
        self._max = (max_offline, max_online)
        return self._max

    @property
    def min(self):
        # с помощью генераторов списка выбираем нужные значения в словаре
        # затем ищем среди них минимальные значения с помощью функции min
        min_offline = min(i['Offline'] for i in self._data)
        min_online = min(i['Online'] for i in self._data)
      
        self._min = (min_offline, min_online)
        return self._min

    @property
    def disp(self):
        # находим дисперсию по формуле
        disp_offline = sum([pow((i['Offline'] - self._mean[0]), 2) for i in self._data]) / len(self._data)

        disp_online = sum([pow((i['Online'] - self._mean[0]), 2) for i in self._data]) / len(self._data)

        self._disp = (disp_offline, disp_online)
        return self._disp

    # по аналогии — со среднем квадратичным отклонением
    @property
    def sigma_sq(self):
        # находим среднее квадратичное отклонение
        # используя полученные значения дисперсии
        self._sigma_sq = (sqrt(self._disp[0]), sqrt(self._disp[1]))
        return self._sigma_sq