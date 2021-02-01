import RPi.GPIO as GPIO

RLED = 28
GLED = 32
YLED = 36
#Buttons are only on 7,11,12,13,15,16,18,22
Button1 = 7
Button2 = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(RLED, GPIO.OUT)
GPIO.setup(GLED, GPIO.OUT)
GPIO.setup(YLED,GPIO.OUT)
GPIO.setup(Button1, GPIO.IN)
GPIO.setup(Button2, GPIO.IN)

counter1 = 0
counter2 = 0

while True:
    input1 = GPIO.input(Button1)
    input2 = GPIO.input(Button2)
    while input1 == False and input2 == False:
        input1 = GPIO.input(Button1)
        input2 = GPIO.input(Button2)
        if input1 == True:
            counter1 += 1
            if counter1 % 2 == 0:
                GPIO.output(RLED,False)
                GPIO.output(GLED,True)
                GPIO.output(YLED,False)
            elif counter1 % 2 == 1:
                GPIO.output(RLED,True)
                GPIO.output(GLED,False)
                GPIO.output(YLED,True)
        if input2 == True:
            counter2 += 1
            if counter2 % 2 == 0:
                GPIO.output(RLED,False)
                GPIO.output(GLED,True)
            elif counter2 % 2 == 1:
                GPIO.output(RLED,True)
