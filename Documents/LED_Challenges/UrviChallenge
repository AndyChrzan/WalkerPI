#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

colors = [0xFF00, 0x00FF, 0x0FF0, 0xF00F] 
	#This is the array used in the method loop and altered by the method setColor
	#0x tells python the value is a hexidecimal literal
	# We THINK this is hexidecmial color values w/out Blue (RR,GG,BB)
	# If so, {[FF],[00]} translates to [(15 x 16^1) + (15 x 16^0)] , [(0 x 16^1) + (0 x 16^0)] 
	# (in other words, {255, 0}... which is full Red, no Green)
	# A.)Try it!  What do 0x00FF, 0x0FF0, and 0xF00F represent?  (answer at end of program.) 

pins = (11, 12)  # pins is a dict

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(pins, GPIO.OUT)   # Set pins' mode is output
GPIO.output(pins, GPIO.LOW)  # Set pins to LOW(0V) to off led

p_R = GPIO.PWM(pins[0], 2000)  # set Frequency to 2KHz		What does frequency do here? Possibly sets intensity? 
			       #PWM: Pulse Width Modulation (Frequency waves)
p_G = GPIO.PWM(pins[1], 2000)  #Uses DMA (Direct Memory Access) for more precision and slower timing

p_R.start(0)      # Initial duty Cycle = 0(leds off)
p_G.start(0)

def map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def setColor(col):   # For example : col = 0x1122
	R_val = col  >> 8		#shifts binary value of col 8 to right, and ignores 8 rightmost values
					#EX: 255 >> 8 = 0?
					#255 in binary = 11111111, shifting all 8 to the right and supplementing 0's
				     	#in front we get 00000000
	G_val = col & 0x00FF
	
	R_val = map(R_val, 0, 255, 0, 100)
	G_val = map(G_val, 0, 255, 0, 100)
	
	p_R.ChangeDutyCycle(R_val)     # Change duty cycle
	p_G.ChangeDutyCycle(G_val)

def loop():
	while True:
		for col in colors:  #col is each index for the array colors defined in line 5.  It's values are 0-3.
			setColor(col)
			time.sleep(0.5)

def destroy():
	p_R.stop()
	p_G.stop()
	GPIO.output(pins, GPIO.LOW)    # Turn off all leds
	GPIO.cleanup()

if __name__ == "__main__":
	try:
		loop()
	except KeyboardInterrupt:
		destroy()

#A.) 0x00FF = 0, 255 (Full Green), 0x0FF0 = 15,240 (15 Red, 240 Green)  0xF00F (240 Red, 15 Green)
