import RPi.GPIO as GPIO
import time
import urllib2
import json
import time
import Adafruit_DHT
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn import preprocessing
import pandas as pd
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.IN) #gas
#GPIO.setup(3,GPIO.OUT)#motor(optional)
GPIO.setup(17,GPIO.IN) #soil
#GPIO.setup(27,GPIO.IN)
sensor = Adafruit_DHT.DHT11




def sendNotification(token, channel, message):
	data = {
		"body" : message,
		"message_type" : "text/plain"
	}

	req = urllib2.Request('http://api.pushetta.com/api/pushes/{0}/'.format(channel))
	req.add_header('Content-Type', 'application/json')
	req.add_header('Authorization', 'Token {0}'.format(token))

	response = urllib2.urlopen(req, json.dumps(data))




while(True):
	x=GPIO.input(2)
	y=GPIO.input(17)

	if x==0 and y==0 :
		print("gas detected")
		print("moisture detected")
		try:
			print("Reading PIR status")


			sendNotification("7f6fc5b7b41bebf3a92c0f92eef4272054eed27b", "piyush5", "fire\n moisture detected ")
			print("fire and moisture")


		except KeyboardInterrupt:
			print("Exit")

			GPIO.cleanup()

	elif x==0 and y==1:
		print("gas present")
		try:
			print("Reading PIR status")

			sendNotification("7f6fc5b7b41bebf3a92c0f92eef4272054eed27b", "piyush5", "firedetected ")
			print("fire ")


		except KeyboardInterrupt:
			print("Exit")

			GPIO.cleanup()
	elif x==1 and y==0 :
		print("soil detected")
		try:
			print("Reading PIR status")

			sendNotification("7f6fc5b7b41bebf3a92c0f92eef4272054eed27b", "piyush5", "moisture detected ")
			print("moisture ")


		except KeyboardInterrupt:
			print("Exit")

			GPIO.cleanup()
	else:
		print("no  input from the sensors")
		time.sleep(1)
		GPIO.output(3,GPIO.LOW)
		GPIO.output(27,GPIO.LOW)

		#machinelearning:
	while (True):
		# Try to grab a sensor reading.  Use the read_retry method which will retry up
		# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
		humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

		# Note that sometimes you won't get a reading and
		# the results will be null (because Linux can't
		# guarantee the timing of calls to read the sensor).
		# If this happens try again!




		if humidity is not None and temperature is not None:
			print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
			fahrenheit=(temperature × 9/5) + humidity  #formula
			X = df[['HUMIDITY', 'TEMPERATURE']]
			y = df['WEATHER FORECAST']
			le = preprocessing.LabelEncoder()#making LabelEncoder function varibale
			df = df.apply(le.fit_transform)#this is used to convert string values into integer values
			reg = linear_model.LinearRegression()
			reg.fit(df[['HUMIDITY', 'TEMPERATURE']], df['WEATHER FORECAST'])

			#print(reg.predict([[humidity,fahrenheit]]))


			if(float(reg.predict([[humidity,fahrenheit]]))>0 and float(reg.predict([[humidity,fahrenheit]]))<1):
				print("")
			try:


				sendNotification("7f6fc5b7b41bebf3a92c0f92eef4272054eed27b", "piyush5", "firedetected ")
				print("fire ")


			except KeyboardInterrupt:
				print("Exit")

				GPIO.cleanup()


			elif(float(reg.predict([[humidity,fahrenheit]]))>1 and float(reg.predict([[humidity,fahrenheit]]))<2):
			try:
				print("Reading PIR status")

				sendNotification("7f6fc5b7b41bebf3a92c0f92eef4272054eed27b", "piyush5", "firedetected ")
				print("fire ")


			except KeyboardInterrupt:
				print("Exit")

				GPIO.cleanup()


			elif (float(reg.predict([[humidity, fahrenheit]])) > 2 and float(reg.predict([[humidity, fahrenheit]])) < 3):
			try:
				print("Reading PIR status")

				sendNotification("7f6fc5b7b41bebf3a92c0f92eef4272054eed27b", "piyush5", "firedetected ")
				print("fire ")


			except KeyboardInterrupt:
				print("Exit")

				GPIO.cleanup()


			elif (float(reg.predict([[humidity, fahrenheit]])) > 3 and float(reg.predict([[humidity, fahrenheit]])) < 4):
			try:
				print("Reading PIR status")

				sendNotification("7f6fc5b7b41bebf3a92c0f92eef4272054eed27b", "piyush5", "firedetected ")
				print("fire ")


			except KeyboardInterrupt:
				print("Exit")

				GPIO.cleanup()


			elif (float(reg.predict([[humidity, fahrenheit]])) > 4 and float(reg.predict([[humidity, fahrenheit]])) < 5):
			try:
				print("Reading PIR status")

				sendNotification("7f6fc5b7b41bebf3a92c0f92eef4272054eed27b", "piyush5", "firedetected ")
				print("fire ")


			except KeyboardInterrupt:
				print("Exit")

				GPIO.cleanup()


			elif (float(reg.predict([[humidity, fahrenheit]])) > 5 and float(reg.predict([[humidity, fahrenheit]])) < 6):
			try:
				print("Reading PIR status")

				sendNotification("7f6fc5b7b41bebf3a92c0f92eef4272054eed27b", "piyush5", "firedetected ")
				print("fire ")


			except KeyboardInterrupt:
				print("Exit")

				GPIO.cleanup()


			elif (float(reg.predict([[humidity, fahrenheit]])) > 6 and float(reg.predict([[humidity, fahrenheit]])) < 7):
			try:
				print("Reading PIR status")

				sendNotification("7f6fc5b7b41bebf3a92c0f92eef4272054eed27b", "piyush5", "firedetected ")
				print("fire ")


			except KeyboardInterrupt:
				print("Exit")

				GPIO.cleanup()


			elif (float(reg.predict([[humidity, fahrenheit]])) > 7 and float(reg.predict([[humidity, fahrenheit]])) < 8):
			try:
				print("Reading PIR status")

				sendNotification("7f6fc5b7b41bebf3a92c0f92eef4272054eed27b", "piyush5", "firedetected ")
				print("fire ")


			except KeyboardInterrupt:
				print("Exit")

				GPIO.cleanup()


			elif (float(reg.predict([[humidity, fahrenheit]])) > 8 and float(reg.predict([[humidity, fahrenheit]])) < 9):
			try:
				print("Reading PIR status")

				sendNotification("7f6fc5b7b41bebf3a92c0f92eef4272054eed27b", "piyush5", "firedetected ")
				print("fire ")


			except KeyboardInterrupt:
				print("Exit")

				GPIO.cleanup()


			elif (float(reg.predict([[humidity, fahrenheit]])) > 9 and float(reg.predict([[humidity, fahrenheit]])) < 10):
			try:
				print("Reading PIR status")

				sendNotification("7f6fc5b7b41bebf3a92c0f92eef4272054eed27b", "piyush5", "firedetected ")
				print("fire ")


			except KeyboardInterrupt:
				print("Exit")

				GPIO.cleanup()


			elif (float(reg.predict([[humidity, fahrenheit]])) > 10 and float(reg.predict([[humidity, fahrenheit]])) < 11):
			try:
				print("Reading PIR status")

				sendNotification("7f6fc5b7b41bebf3a92c0f92eef4272054eed27b", "piyush5", "firedetected ")
				print("fire ")


			except KeyboardInterrupt:
				print("Exit")

				GPIO.cleanup()


			else:
				print("not predicted")
		else:
			print('Failed to get reading. Try again!')

		time.sleep(3)

