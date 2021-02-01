#This program will turn on a light at the push of a button and will turn it
#off at the second push

import RPi.GPIO as GPIO
import time

LED = 11
button = 15
run = True

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(button,GPIO.IN)

input = GPIO.input(button)

while run:
    if input:
        GPIO.output(LED,True)
        while input:
            if(input==False):
                GPIO.output(LED,False)
                run = False

GPIO.cleanup()

