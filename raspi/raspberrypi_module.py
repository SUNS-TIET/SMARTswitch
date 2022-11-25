import RPi.GPIO as GPIO
import time, sys
import os
import requests
import json

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

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
		start_counter = 1
		time.sleep(1)
		start_counter = 0
		flow = (count / 7.5) # Pulse frequency (Hz) =7.5Q, Q is flow rate in L/min.
		print("The flow is: %.3f Liter/min" % (flow))
		#os.system ("'curl -X PUT -d '{"time": current_time ,"flow": flow}' 'https://hackathon-42f90-default-rtdb.firebaseio.com/data.json'")

		#publish.single("/Garden.Pi/WaterFlow", flow, hostname=MQTT_SERVER)
		

		headers = {
		  	'Content-Type': 'application/x-www-form-urlencoded',
		 }

		data = {"time": current_time ,"flow": flow}
		data_json = json.dumps(data)

		response = requests.put('https://hackathon-42f90-default-rtdb.firebaseio.com/data.json', headers=headers, data=data_json)
		count = 0
		time.sleep(5)
	except KeyboardInterrupt:
		print('\nkeyboard interrupt!')
	GPIO.cleanup()
	sys.exit() #shouldn't be used i guess
	