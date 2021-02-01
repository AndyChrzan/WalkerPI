#This program blinks an LED while asserting a postive voltage from both sides.
#The schematic for this program is found on pg 24 of  the Sunfounder book.
import RPi.GPIO as GPIO
import time

LED = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED,GPIO.OUT)
GPIO.output(LED,GPIO.HIGH)

try:
	while True:
		print '...LED on'
		GPIO.output(LED,GPIO.LOW)
		time.sleep(.5)
		print 'LED off...'
		GPIO.output(LED,GPIO.HIGH)
		time.sleep(.5)

except KeyboardInterrupt:
	GPIO.output(LED,GPIO.HIGH)
	GPIO.cleanup()
