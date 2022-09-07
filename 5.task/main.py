import json
import requests

api_key = "a6713e45-d989-4b6b-9333-84305c3df12f" 
url = "https://api.weather.yandex.ru/v2/forecast"

def get_weather_week(lat, lon):
    
    weather = dict()

    url = 'https://api.weather.yandex.ru/v2/forecast' 
    req = requests.get(
        url, 
        params = {
            "lat": str(lat),
            "lon": str(lon)
        },
        headers = { "X-Yandex-API-Key": api_key }
        )

    req_obj = json.loads(req.text)  

    days_lst = [obj for obj in req_obj["forecasts"]] 

    for day in days_lst:
        weather[day["date"][5:10]] = day["parts"]["day"]["temp_avg"] 
    
    return weather

def get_weather_hours(lat, lon):
    
    weather = dict()

    url = 'https://api.weather.yandex.ru/v2/forecast'
    req = requests.get(
        url, 
        params = {
            "lat": str(lat),
            "lon": str(lon)
        },
        headers = { "X-Yandex-API-Key": api_key }
        )

    req_obj = json.loads(req.text)  

    days_lst = [(obj["date"], obj["hours"]) for obj in req_obj["forecasts"]]  
    
    days_lst = [obj for obj in req_obj["forecasts"]] 
    for day in days_lst:
        for hour in day['hours']:
            weather[str(day["date"][5:10]) + " " + str(hour['hour']) + "ч"] = hour["temp"] 

    return weather

def vizualize_data(weather):
    import matplotlib.pyplot as pplt

    dates = list(weather.keys())
    values = list(weather.values())

    pplt.xlabel("Dates")
    pplt.ylabel("Temps")
    pplt.scatter(dates, values)

    pplt.show()

if __name__ == "__main__":
    vizualize_data(get_weather_week(55.45, 37.36))
    vizualize_data(get_weather_hours(55.45, 37.36))
