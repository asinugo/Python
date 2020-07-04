from gpiozero import DistanceSensor import LED
from time import sleep #import DistanceSensor,sleep, LED modules from time, gpiozero libraries 
#define sensor object
sensor = DistanceSensor(echo=6, trigger=5, max_distance=3)
#initalize infinite loop
while True:
    #display distance in cm 
    print('Distance in centimeters is: ', sensor.distance * 100)
    #trigger every 5 seconds
    sleep(5)