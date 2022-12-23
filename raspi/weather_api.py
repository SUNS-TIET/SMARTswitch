import datetime as dt 
import requests
import json

BASE_URL = "https://api.agromonitoring.com/agro/1.0/weather"

appid = "INSERT APP ID HERE" #this is my appid CHANGE IT

def get_weather_data(lat, lon, start):
	url = f'{BASE_URL}?lat={lat}&lon={lon}&units=metric&appid={appid}'
	r = requests.get(url)
	return r.json()

weather_patiala = (get_weather_data(30.3398, 76.3869, appid)) #patiala longitude and latitude
weather_chandigarh = (get_weather_data(30.7333, 76.7794, appid))
weather_amritsar = (get_weather_data(31.6340, 74.8723, appid))
