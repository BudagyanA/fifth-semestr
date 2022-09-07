import requests
import json
import csv
from bs4 import BeautifulSoup

class BaseComponent(): 
  def get_currencies():
    pass

class Decorator(BaseComponent): 
    __component = BaseComponent() 

    def __init__(self, component):
        self.__component = component 

class DecoratorJSON(Decorator): 
    __component = BaseComponent() 

    def __init__(self, component): 
        self.__component = component 

    def dict_to_json(self):
        dct = self.__component.get_currencies(["R01090B", "R01720", "R01565"])
        with open('result.json', 'w') as fp:
            json.dump(dct, fp, indent = 4, ensure_ascii=False)

class DecoratorCSV(Decorator): 
    __component = BaseComponent()

    def __init__(self, component): 
        self.__component = component 

    def dict_to_csv(self):
        dct = self.__component.get_currencies(["R01090B", "R01720", "R01565"])
        with open('result.csv', 'w') as fp:
            w = csv.DictWriter(fp, dct.keys())
            w.writeheader()
            w.writerow(dct)
    
class CurrenciesList(BaseComponent):

    def get_currencies(self, currencies_ids_lst=None):
        if currencies_ids_lst is None:
            currencies_ids_lst = [
                'R01239', 'R01235', 'R01035', 'R01815', 'R01585F', 'R01589',
                'R01625', 'R01670', 'R01700J', 'R01710A'
            ]
        cur_res_str = requests.get("http://www.cbr.ru/scripts/XML_daily.asp").text
        result={}
        soup = BeautifulSoup(cur_res_str, 'html.parser')

        valutes = soup.find_all("valute")
        for _v in valutes:
            valute_id = _v['id']
            
            if str(valute_id) in currencies_ids_lst:
                valute_cur_val = _v.find('value').string
                valute_cur_name = _v.find('name').string

                result[valute_id] = (valute_cur_val, valute_cur_name)
        return result

cur_lst = DecoratorJSON(CurrenciesList()) 
cur_lst.dict_to_json() 

cur_lst = DecoratorCSV(CurrenciesList()) 
cur_lst.dict_to_csv()
