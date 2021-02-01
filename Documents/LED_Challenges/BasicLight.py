#This is our first working program to light an LED with a button.
#This setup 

import RPi.GPIO as GPIO

LED = 16
Button = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(LED,GPIO.HIGH)
GPIO.setup(Button,GPIO.IN)
counter = 0
GPIO.output(LED,False)
while True:
    input_value = GPIO.input(Button)
    while input_value == False:
        input_value = GPIO.input(Button)
        if input_value == True:
            counter += 1
        if counter % 2 == 0:
            GPIO.output(LED,False)
        elif counter % 2 == 1:
            GPIO.output(LED,True)

        
