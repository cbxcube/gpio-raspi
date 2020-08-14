
# source : 
# https://www.youtube.com/watch?v=lOb4G8Le9fQ

from time import sleep
import RPi.GPIO as GPIO


# to use physical pins :
GPIO.setmode(GPIO.BOARD)

button1=16
button2=12

# setup buttons 
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)

# run
# read status of button1 (pressed/not pressed:1/0)
while(1):
		if GPIO.input(button1)==0:
				print "Button 1 Was Pressed:"
				# Slow down output
				sleep(.1)
		if GPIO.input(button2)==0:
				print "Button 2  Was Pressed:"
				# Slow down output
				sleep(.1)
			
	
