# This program takes a picture using the Pi Camera and saves it to a file.
# Spring 2020
# CIT 394 - Internet of Things

# Import needed modules
from picamera import PiCamera

# Set the path and name of the photo
file = "/home/pi/Pictures/cit394.jpg" # Change this to whatever you would like

# Create the camera object.

camera = PiCamera()

# Optionally we can set things like the resolution
camera.resolution = (3280,2464) # Maximum resolution

camera.capture(file) # Takes the picture
camera.stop_preview()  # Removes the preview from the GUI
