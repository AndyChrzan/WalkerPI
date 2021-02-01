#This program will cause a light to turn on, stay on for two seconds,
#and then turn off for one second

import RPi.GPIO as GPIO
import time

LED = 11 #Pin 16 is not functional
count = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED,GPIO.OUT)

while count<5: #Have light flicker on and off
    GPIO.output(LED,True)
    print 'on' #Debug
    time.sleep(.5)
    GPIO.output(LED,False)
    print 'off' #Debug
    time.sleep(1)
    count = (count+1)

GPIO.output(LED,False) #Ensure light is off
GPIO.cleanup() #Clear board

