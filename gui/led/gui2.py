from Tkinter import *
import tkFont
import RPi.GPIO as GPIO


# Changing to from GPIO.BOARD to GPIO.BCM
# GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
# 
# testing - Adding cleanup
# GPIO.cleanup()
#
# Changing ports from 40 to 17 and 27 as in workshop  
# GPIO.setup(40, GPIO.OUT)
# GPIO.output(40, GPIO.LOW)
# LED1:
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.LOW)
# LED2:
GPIO.setup(27, GPIO.OUT)
GPIO.output(27, GPIO.LOW)
# BEEP/Buzzer:
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.LOW)

win = Tk()

myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')

def ledON1():
	print("LED1 button pressed")
	if GPIO.input(17) :
 		GPIO.output(17,GPIO.LOW)
		ledButton1["text"] = "LED1 ON"
	else:
		GPIO.output(17,GPIO.HIGH)
                ledButton1["text"] = "LED1 OFF"

def ledON2():
	print("LED2 button pressed")
	if GPIO.input(27) :
 		GPIO.output(27,GPIO.LOW)
		ledButton2["text"] = "LED2 ON"
	else:
		GPIO.output(27,GPIO.HIGH)
                ledButton2["text"] = "LED2 OFF"

def beepON():
	print("Beep button pressed")
	if GPIO.input(22) :
 		GPIO.output(22,GPIO.LOW)
		beepButton["text"] = "BEEP ON"
	else:
		GPIO.output(22,GPIO.HIGH)
                beepButton["text"] = "BEEP OFF"

def exitProgram():
	print("Exit Button pressed")
        GPIO.cleanup()
	win.quit()	


win.title("Workshop Kit Console")
win.geometry('800x480')

exitButton  = Button(win, text = "Exit", font = myFont, command = exitProgram, height =2 , width = 6) 
exitButton.pack(side = BOTTOM)

ledButton1 = Button(win, text = "LED1 ON", font = myFont, command = ledON1, height = 2, width =8 )
ledButton1.pack()

ledButton2 = Button(win, text = "LED2 ON", font = myFont, command = ledON2, height = 2, width =8 )
ledButton2.pack()

beepButton = Button(win, text = "BEEP ON", font = myFont, command = beepON, height = 2, width =8 )
beepButton.pack()
mainloop()
