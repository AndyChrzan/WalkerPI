import RPi.GPIO as GPIO
import time

Red_Main = 7
Green_Main = 15
Yellow_Main = 11
Red_Side = 32
Green_Side = 36
Yellow_Side = 22
Button = 29

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Red_Main,GPIO.OUT)
GPIO.setup(Green_Main,GPIO.OUT)
GPIO.setup(Yellow_Main,GPIO.OUT)
GPIO.setup(Red_Side,GPIO.OUT)
GPIO.setup(Green_Side,GPIO.OUT)
GPIO.setup(Yellow_Side,GPIO.OUT)
GPIO.setup(Button,GPIO.IN)


GPIO.output(Red_Main,False)
GPIO.output(Green_Main,True)
GPIO.output(Yellow_Main,False)
GPIO.output(Red_Side,True)
GPIO.output(Green_Side,False)
GPIO.output(Yellow_Side,False)

while True:
    input_value = GPIO.input(Button)
    while input_value == False:
        input_value == GPIO.input(Button)
        if input_value == True:
            GPIO.output(Green_Main,False)
            GPIO.output(Yellow_Main,True)
            time.sleep(2)
            GPIO.output(Yellow_Main,False)
            GPIO.output(Red_Main,True)
            GPIO.output(Red_Side,False)
            GPIO.output(Green_Side,True)
            time.sleep(10)
            GPIO.output(Green_Side,False)
            GPIO.output(Yellow_Side,True)
            time.sleep(2)
            GPIO.output(Yellow_Side,False)
            GPIO.output(Red_Side,True)
            GPIO.output(Red_Main,False)
            GPIO.output(Green_Main,True)
            


    
