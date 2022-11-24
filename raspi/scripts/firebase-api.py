import pyrebase
import Github.SMARTswitch.raspi.raspberrypi_module as raspberrypi_module
import os
os.system ('curl -X PUT -d '{"date":"24 November 2022","humidity":"50%","moisture":"25%","pump":"OFF","temp":"20°C","time":"19:51","water_l":"20 m"}' 'https://hackathon-42f90-default-rtdb.firebaseio.com/data.json'')

config = {
  "apiKey": "AIzaSyCrnBv4H_bVrggc756az9OuqKrFP6mkLjk",
  "authDomain": "http://hackathon-42f90.firebaseapp.com",
  "databaseURL": "https://hackathon-42f90-default-rtdb.firebaseio.com",
  "storageBucket": "projectId.appspot.com",
  "projectId": "hackathon-42f90",
  "storageBucket": "hackathon-42f90.appspot.com",
  "messagingSenderId": "712245767976",
  "appId": "1:712245767976:web:3a082edfb5d07ca63caa1d"

}

firebase = pyrebase.initialize_app(config)
curl -X PUT -d '{"date":"24 November 2022","humidity":"50%","moisture":"25%","pump":"OFF","temp":"20°C","time":"19:51","water_l":"20 m"}' 'https://hackathon-42f90-default-rtdb.firebaseio.com/data.json'