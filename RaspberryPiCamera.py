1st Program: # Chinedu Asinugo 
# Professor Ken Roth
# Lab 11 
# Spring 2020
# CIT 394 - Internet of Things
#This program takes a picture using the Pi Camera and saves it to a file.
Import needed modules
from picamera import PiCamera

# Set the path and name of the photo
file = "/home/pi/Pictures/cit394.jpg" 
# Create the camera object.

camera = PiCamera()

# Optionally we can set things like the resolution
camera.resolution = (3280,2464) # Maximum resolution

camera.capture(file) # Takes the picture
camera.stop_preview()  # Removes the preview from the GUI



2nd Program: 
# Chinedu Asinugo 
# Professor Ken Roth
# Lab 11 
# Spring 2020
# CIT 394 - Internet of Things
#This program takes a picture based on motion detected, and saves it to a file. 


# Import needed modules
from picamera import PiCamera
from gpiozero import Button
from gpiozero import LED
import time

#assigning motion sensor 
motion = MotionSensor(21)

# assigning led object
led = LED(19, active_high = False) 

# set LED to an initial state of 'off'
led.off()

# Create the camera object.
camera = PiCamera()

# Set the path and name of the photo
file = "/home/pi/Pictures/cit394.jpg" 

camera.resolution = (3280,2464) # Maximum resolution

def motionDetect():
	#define global variables used
	global led 
	global camera 
	global file
	led.on()
	camera.capture(file) # Takes the picture
	camera.stop_preview()  # Removes the preview from the GUI
	led.off()
	time.sleep(1.0)
	
while True:
# Define actions to take when motion is detected 
        motion.when_motion = motionDetect
#pause the script for 2 seconds to reduce number of pictures taken 
	motion.wait_for_motion(timeout=2.0)
2.	Submit your extra credit program if you do that part of the lab to Canvas.
# Chinedu Asinugo 
# Professor Ken Roth
# Lab 11 
# Spring 2020
# CIT 394 - Internet of Things
#This program takes a picture based on motion detected, and saves it to a file 
#which has a time stamp apended to it. 

# Import needed modules
from picamera import PiCamera
from gpiozero import Button
from gpiozero import LED
import time
import datetime

#assigning motion sensor 
motion = MotionSensor(21)

# assigning led object
led = LED(19, active_high = False) 

# set LED to an initial state of 'off'
led.off()

# Create the camera object.
camera = PiCamera()

#define time elements 
now = datetime.datetime.now()
#format date 
date = now.strftime("%Y%m%d%H%M%S")


# Set the path and name of the photo
file = "/home/pi/Pictures/cit394_"+date+".jpg"

camera.resolution = (3280,2464) # Maximum resolution

def motionDetect():
	#define global variables used
	global led 
	global camera 
	global file
	led.on()
	camera.capture(file) # Takes the picture
	camera.stop_preview()  # Removes the preview from the GUI
	led.off()
	time.sleep(1.0)
	

while True:
# Define actions to take when motion is detected 
        motion.when_motion = motionDetect
#pause the script for 2 seconds to reduce number of pictures taken 
	motion.wait_for_motion(timeout=2.0)
s