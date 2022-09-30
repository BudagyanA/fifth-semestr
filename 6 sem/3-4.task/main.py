# Программирование (Python)
# 6 семестр, тема 1

# Лабораторная работа 2
"""
Используя обучающий набор данных о пассажирах Титаника, находящийся в проекте (оригинал: https://www.kaggle.com/c/titanic/data), найдите ответы на следующие вопросы: 

1. Какое количество мужчин и женщин ехало на пароходе? Приведите два числа через пробел.

2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.

3. Посчитайте долю (процент) погибших на пароходе (число и процент)?

4. Какие доли составляли пассажиры первого, второго, третьего класса?

5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).

6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
1) возрастом и параметром Survived;
2) полом человека и параметром Survived;
3) классом, в котором пассажир ехал, и параметром Survived.

7. Посчитайте средний возраст пассажиров и медиану.
8. Посчитайте среднюю цену за билет и медиану.

9. Какое самое популярное мужское имя на корабле?
10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?


Для вычисления 3, 4, 5, 6, 7, 8 используйте тип данных float с точностью два знака в дробной части. 
"""

import pandas as pd
from numpy import isnan


def get_sex_distrib(data):
    """
    1. Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.
    """

    n_male, n_female = data['Sex'].value_counts() 
    return f"{n_male}, {n_female}" 


def get_port_distrib(data):
    """  
    2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.
    """

    port_S, port_C, port_Q = data['Embarked'].value_counts() 
    return f"{port_S}, {port_C}, {port_Q}"


def get_surv_percent(data):
    """
    3. Посчитайте долю погибших на пароходе (число и процент)?
    """

    n_died = data['Survived'].value_counts()[0]

    perc_died = data['Survived'].value_counts(normalize=True)[0]*100

    return f"{n_died}, {perc_died:.2f}%" 


def get_class_distrib(data):
    """
    4. Какие доли составляли пассажиры первого, второго, третьего класса?    
    """
    n_pas_f_cl, n_pas_s_cl, n_pas_t_cl = data['Pclass'].value_counts(normalize=True) * 100 

    return f"{n_pas_f_cl:.2f}, {n_pas_s_cl:.2f}, {n_pas_t_cl:.2f}"


def find_corr_sibsp_parch(data):
    """
    5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).
    """

    sibsp = []
    parch = []

    i = 0
    while i < len(data):    

        if not(isnan(data.iloc[i]['SibSp'])): 

            sibsp.append(data.iloc[i]['SibSp']) 
            parch.append(data.iloc[i]['Parch']) 

        i += 1

    sibsp = pd.Series(sibsp)  
    parch = pd.Series(parch)

    corr_val = sibsp.corr(parch)
    return f"{corr_val:.2f}"


def find_corr_age_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    
    - возрастом и параметром Survived;

    """
  
    age = []
    survived = []
    
    i = 0
    while i < len(data):

        if not(isnan(data.iloc[i]['Age'])):
            age.append(data.iloc[i]['Age'])
            survived.append(data.iloc[i]['Survived'])
        
        i += 1

    age = pd.Series(age)
    survived = pd.Series(survived)

    corr_val = age.corr(survived)
    
    return f"{corr_val:.2f}"


def find_corr_sex_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    
    - полом человека и параметром Survived;
    """

    sex = []
    survived = []
    
    i = 0
    while i < len(data):

        if not(isnan(data.iloc[i]['Survived'])):
            
            if data.iloc[i]['Sex'] == "male":
                sex.append(0)
            else:
                sex.append(1)

            survived.append(data.iloc[i]['Survived'])
        
        i += 1

    sex = pd.Series(sex)
    survived = pd.Series(survived)

    corr_val = sex.corr(survived)
  
    return f"{corr_val:.2f}"


def find_corr_class_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:

    - классом, в котором пассажир ехал, и параметром Survived.
    """
    
    pclass = []
    survived = []
    
    i = 0
    while i < len(data):

        if not(isnan(data.iloc[i]['Pclass'])):
            pclass.append(data.iloc[i]['Pclass'])
            survived.append(data.iloc[i]['Survived'])
        i += 1

    pclass = pd.Series(pclass) 
    survived = pd.Series(survived)
    
    corr_val = pclass.corr(survived)
    
    return f"{corr_val:.2f}"


def find_pass_mean_median(data):
    """
    7. Посчитайте средний возраст пассажиров и медиану.
    """

    mean_age, median = data['Age'].mean(), data['Age'].median()
    
    return f"{mean_age:.2f}, {median:.2f}"


def find_ticket_mean_median(data):
    """
    8. Посчитайте среднюю цену за билет и медиану.
    """
    mean_price, median = data['Fare'].mean(), data['Fare'].median()
    
    return f"{mean_price:.2f}, {median:.2f}"


from collections import Counter 

def find_popular_name(data):
    """
    9. Какое самое популярное мужское имя на корабле?
    """
    names = []

    for i in data.iloc:
        
        if i['Sex'] == "male":

            name = i['Name'].partition('. ')[2].split(' ')

            names.append(name[0])

    res = Counter(names).most_common(1)

    return f"{res[0][0]}"


def find_popular_adult_names(data):
    """
    10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?
    """

    male = []
    female = []

    for i in data.iloc:

        if i['Age'] > 15 and i['Sex'] == 'male':
            
            name = i['Name'].partition('. ')[2].split(' ')

            male.append(name[0]) 

        elif i['Age'] > 15 and i['Sex'] == 'female':
            
            if '(' in i['Name']:

                name = i['Name'].partition('(')[2].rstrip(')').split(' ')
            
            else:
                name = i['Name'].partition('. ')[2].split(' ')

            female.append(name[0])

    popular_male_name = Counter(male).most_common(1)
    popular_female_name = Counter(female).most_common(1)
    
    return f"{popular_male_name[0][0]}, {popular_female_name[0][0]}"


'''
Часть 2. Для набора данных из лабораторной работы 1 посчитать средние значения, 
медианы, максимальные и минимальные значения для столбцов Offline Spend, Online Spend.
'''

def find_mean_median(data, column):
    mean, median = data[column].mean(), data[column].median()
    return f"{mean:.2f}, {median:.2f}"

def find_max_min(data, column):
    max, min = data[column].max(), data[column].min()
    return f"{max}, {min}"



if __name__ == "__main__":

    data = pd.read_csv('train.csv', index_col="PassengerId")
    mark_spend = pd.read_csv('MarketingSpend.csv')
    
    # Часть 1
    print('1. ', get_sex_distrib(data))
    print('2. ', get_port_distrib(data))
    print('3. ', get_surv_percent(data))
    print('4. ', get_class_distrib(data))
    print('5. ', find_corr_sibsp_parch(data))
    print('6.1. ', find_corr_age_survival(data))
    print('6.2. ', find_corr_sex_survival(data))
    print('6.3. ', find_corr_class_survival(data))
    print('7. ', find_pass_mean_median(data))
    print('8. ', find_ticket_mean_median(data))
    print('9. ', find_popular_name(data))
    print('10. ', find_popular_adult_names(data))

    # Часть 2
    print("Offline, среднее и медиана: ", find_mean_median(mark_spend, 'Offline Spend'))
    print("Online, среднее и медиана: ", find_mean_median(mark_spend, 'Online Spend'))
    
    print("Offline, максимальное и минимальное: ", find_max_min(mark_spend, 'Offline Spend'))
    print("Online: максимальное и минимальное", find_max_min(mark_spend, 'Online Spend'))

#-------------------------------------------------------
  
# Тесты
def test_get_sex_distrib():
    assert get_sex_distrib(data) == "577, 314"


def test_get_port_distrib():
    assert get_port_distrib(data) == "644, 168, 77"


def test_get_surv_percent():
    assert get_surv_percent(data) == "549, 61.62%"


def test_get_class_distrib():
    assert get_class_distrib(data) == "55.11, 24.24, 20.65"


def test_find_corr_sibsp_parch():
    assert find_corr_sibsp_parch(data) == "0.41"


def test_find_corr_age_survival():
    assert find_corr_age_survival(data) == "-0.08"


def test_find_corr_sex_survival():
    assert find_corr_sex_survival(data) == "0.54"


def test_find_corr_class_survival():
    assert find_corr_class_survival(data) == "-0.34"


def test_find_pass_mean_median():
    assert find_pass_mean_median(data) == "29.70, 28.00"


def test_find_ticket_mean_median():
    assert find_ticket_mean_median(data) == "32.20, 14.45"


def test_find_popular_name():
    assert find_popular_name(data) == "John"


def test_find_popular_adult_names():
    assert find_popular_adult_names(data) == "William, Anna"