#This module helps communicate with raspberry pi for SOIL SENSORS, WATER FLOW SENSOR,
import RPi.GPIO as GPIO
import time, sys
import os
import requests
import json
import weather_api as wa
import datetime


FLOW_SENSOR_GPIO = 13
#MQTT_SERVER = "192.168.1.220"

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR_GPIO, GPIO.IN, pull_up_down = GPIO.PUD_UP)

global count
count = 0

def countPulse(channel):
	global count
	if start_counter == 1:
		count = count+1

GPIO.add_event_detect(FLOW_SENSOR_GPIO, GPIO.FALLING, callback=countPulse)

while True:
	try:

		t = time.localtime()
		current_time = time.strftime("%H:%M:%S", t)

		now = datetime.datetime.now()
		current_date = now.strftime("%Y-%m-%d")


		start_counter = 1
		time.sleep(1)
		start_counter = 0
		flow = (count / 7.5) # Pulse frequency (Hz) =7.5Q, Q is flow rate in L/min.
		print("The flow is: %.3f Liter/min" % (flow))
		print("Sending API Requests...")
		#os.system ("'curl -X PUT -d '{"time": current_time ,"flow": flow}' 'INSERT API LINK HERE'")

		#publish.single("/Garden.Pi/WaterFlow", flow, hostname=MQTT_SERVER)
		

		headers = {
		  	'Content-Type': 'application/x-www-form-urlencoded',
		 }

		data = {"date": current_date ,"water_l":"270 m","moisture":"20 %","pump":"ON","time": current_time ,"flow": flow, "weather": wa.weather_patiala, "temp": wa.weather_patiala["main"]["temp"], "humidity": wa.weather_patiala["main"]["humidity"]}
		data_json = json.dumps(data)
		response = requests.put('INSERT API LINK HERE', headers=headers, data=data_json)
		print("Request Sent to Patiala Firebase API")

		data_chd = {"date": current_date ,"time": current_time ,"flow": flow, "weather": wa.weather_chandigarh, "temp": wa.weather_chandigarh["main"]["temp"], "humidity": wa.weather_chandigarh["main"]["humidity"]}
		data_json_chd = json.dumps(data_chd)
		response = requests.put('INSERT API LINK HERE', headers=headers, data=data_json_chd)
		print("Request Sent to Chandigarh Firebase API")



		data_amritsar = {"date": current_date ,"time": current_time ,"flow": flow, "weather": wa.weather_amritsar, "temp": wa.weather_amritsar["main"]["temp"], "humidity": wa.weather_amritsar["main"]["humidity"]}
		data_json_amritsar = json.dumps(data_amritsar)
		response = requests.put('INSERT API LINK HERE', headers=headers, data=data_json_amritsar)
		print("Request Sent to Amritsar Firebase API")






		# response = requests.put('INSERT API LINK HERE', headers=headers, data=data_json) old url

		count = 0
		time.sleep(60)
		continue
		
	except KeyboardInterrupt:
		print("KeyboardInterrupt has been caught.")
		GPIO.cleanup() #shouldn't be used i guess
		sys.exit()
