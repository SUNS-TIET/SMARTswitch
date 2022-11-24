import datetime as dt 
import requests
import json

BASE_URL = "https://api.agromonitoring.com/agro/1.0/weather"

appid = "f7a11ade0aa0ab4b018fc115bdce8d42" #this is my appid CHANGE IT

def get_weather_data(lat, lon, start):
	url = f'{BASE_URL}?lat={lat}&lon={lon}&units=metric&appid={appid}'
	r = requests.get(url)
	return r.json()

print (get_weather_data(30.3398, 76.3869, appid)) #patiala longitude and latitude