#This program simply turns an LED on for 5 seconds, turns it off,and cleans the board.
#Setup is attached with POS to pin 16(GPIO 23), and NEG in series to a 220 Ohm Resistor, then GND.

import RPi.GPIO as GPIO  	#Tells PYTHON we're working with a Raspberry Pi and that we're going to use input/output pins.
import time 			#Tells PYTHON we're going to use some sort of timing mechanism.

LED = 16 			#Creates a variable called "LED" and sets it equal to 16.

GPIO.setmode(GPIO.BOARD) 	#Tells PYTHON we want to call pins by their numbers, and not by their processor function.
GPIO.setup(LED,GPIO.OUT) 	#Tells PYTHON to make pin 16 an output pin. (+)
GPIO.output(LED,True) 		#Tells PYTHON to make pin 16 "On", "True", or "High"
time.sleep(5) 			#Tells PYTHON to wait 5 seconds before continuing to read the program.
GPIO.output(LED,False) 		#Tells PYTHON to stop putting voltage out through pin 16.  ("Off", "False" or "Low")
GPIO.cleanup() 			#Resets all pins to unassigned, dormant states.