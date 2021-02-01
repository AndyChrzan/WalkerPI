import RPi.GPIO as GPIO
import time

red = 11
green = 12

GPIO.setmode(GPIO.BOARD) #pin numbers, not functions

GPIO.setup(red, GPIO.OUT) #sets red pin 11 as an output
GPIO.output(red, GPIO.LOW) #sets red pin 11 to low (0V)

GPIO.setup(green, GPIO.OUT) #same as for red above
GPIO.setup(green, GPIO.LOW)


try:
	while True:
            time.sleep(0.5)
            GPIO.output(red, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(green, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(red, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(green, GPIO.LOW)

except KeyboardInterrupt:
	GPIO.output(red,GPIO.LOW)
	GPIO.output(green,GPIO.LOW)
	GPIO.cleanup()
