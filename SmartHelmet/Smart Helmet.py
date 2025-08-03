import RPi.GPIO as GPIO
import time
import blynklib
GPIO.setmode(GPIO.BCM)	# for GPIO numbering, choose BCM  
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.IN)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(2,GPIO.OUT)
GPIO,setup(8,GPIO.OUT)        # Buzzer output
channel = 4			# Vibration Sensor Input #
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
BLYNK_AUTH='_Vm3RzK-XFLX7DgpgV7SNdGhn2xDDT3V'
blynk=blynklib.Blynk(BLYNK_AUTH)
while(True):
blynk.run()
	x=GPIO.input(17)			# IR Sensor Input #
	if x==0:
		print("Power on")
		GPIO.output(2,GPIO.HIGH)		# LED #
blynk.notify("Bike is initiated.")
def callback(channel):
                    if GPIO.input(channel):
blynk.notify("Accident Occurred !!")
                        print "MOVEMENT DETECTED!"
                        GPIO.output(8,GPIO.HIGH)        # Buzzer ON
                    else:
                        print "MOVEMENT NOT DETECTED!"
GPIO.add_event_detect(channel,GPIO.BOTH, bouncetime=300) #let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback) #assign function to GPIO PIN ,Run funtion on change 
	else:
                print("Power off")
GPIO.output(2,GPIO.LOW) #make LED Low
GPIO.output(8,GPIO.LOW) #make Buzzer Low
