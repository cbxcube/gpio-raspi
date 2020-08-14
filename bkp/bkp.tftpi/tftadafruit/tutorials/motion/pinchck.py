import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)


while True:

    if GPIO.output(4) == True:
        print "pin is high"
    else:
        print "pin is low"

    time.sleep(0.500)
