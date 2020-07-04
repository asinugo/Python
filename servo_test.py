# Servo Test Code
# CIT 394 
# Spring 2020
# This code will control a servo moving it between the min, mid and max positions.
from gpiozero import Servo
from time import sleep

servo = Servo(5)

for i in range(0,5):
	print("Moving to minimum position")
	servo.min()
	sleep(1)
	print("Moving to mid position")
	servo.mid()
	sleep(1)
	print("Moving to maximum position")
	servo.max()
	sleep(1)


