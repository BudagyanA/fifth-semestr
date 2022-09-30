import requests

api_key = "0b0c090d4c1c6cfe432a2af8e4c5aa56" # 
url = "http://api.openweathermap.org/data/2.5/weather" # 

def get_weather_data(place, key=api_key):

    res = requests.get( 
        url,
        params = { 
            "q": place,
            "appid": key,
            "units": "metric"  
        }
    )
    return res.text # 
    
    
if __name__ == "__main__":
    print(get_weather_data("Saint Petersburg"))
