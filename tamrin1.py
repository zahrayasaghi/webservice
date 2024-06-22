import requests

url = "https://realtime-crypto-prices.p.rapidapi.com/get_rates"

query = {"symbol":"BTC"}

headers = {
    "X-RapidAPI-Key": "fa2ae83c39msh4ccfd5eeff89d1ep18ae3cjsnaed129db5729",
    "X-RapidAPI-Host": "realtime-crypto-prices.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=query)

print(response.json())
import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': location,
        'appid': api_key,
        'units': 'imperial'
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        return data
    else:
        return "Error: Unable to fetch weather data."

api_key = '141374ebd6564df364cecc798844e7d4'
location = 'New York'

# Get and print the weather report
weather_report = get_weather(api_key, location)
print(weather_report)