import RPi.GPIO as GPIO
import time

RLED = 12
GLED = 13
YLED = 15
#Buttons are only on 7,11,12,13,15,16,18,22
Button1 = 7
Button2 = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(RLED, GPIO.OUT)
GPIO.setup(GLED, GPIO.OUT)
GPIO.setup(YLED, GPIO.OUT)
GPIO.setup(Button1, GPIO.IN)
GPIO.setup(Button2, GPIO.IN)

counter1 = 0
counter2 = 0
counter3 = 0

try:
    while True:
        input1 = GPIO.input(Button1)
        input2 = GPIO.input(Button2)
        while input1 == False and input2 == False:
            input1 = GPIO.input(Button1)
            input2 = GPIO.input(Button2)
            if input1 == True and input2 == False:
                counter1 = counter1 + 1
                print "Button 1 has been pressed"
                if counter1 % 2 == 0:
                    GPIO.output(GLED,False)
                elif counter1 % 2 == 1:
                    GPIO.output(GLED,True)
            if input2 == True and input1 == False:
                counter2 = counter2 + 1
                print "Button 2 has been pressed"
                if counter2 % 2 == 0:
                    GPIO.output(RLED,False)
                elif counter2 % 2 == 1:
                    GPIO.output(RLED,True)
            if input2 == True and input1 == True:
                counter3 = counter3 + 1
                print "Both Buttons have been pressed"
                if counter3 % 2 == 0:
                    GPIO.output(YLED,False)
                elif counter3 % 2 == 1:
                    GPIO.output(YLED,True)
            time.sleep(.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    print "\nBut world domination was within reach..."
