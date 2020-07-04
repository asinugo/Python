#Chinedu Asinugo        
#Lab 2 - Cit 394

from gpiozero import LED #import LED,time modules from gpizero libary
import time
led = LED(17, active_high = False) #initiate an LED object
#create an infinite loop
while True:
    led.on()
    time.sleep(1)
	led.off()
    time.sleep(1) #blink LED object
Time.sleep(5)

Part 2:  
#Chinedu Asinugo        
#Lab 2 - Cit 394

from gpiozero import LED #import LED,time modules from gpizero libary
import time
led = LED(17, active_high = False) #initiate an LED object
#create an infinite loop
while True:
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1) #blink LED object
Time.sleep(5)
