# Example of using events to light LED's accordingly

# Import required modules
from gpiozero import Button, LED
import time

# Declare global variables

# Two LED's are connected to GPIO 17 and GPIO 27
# with the cathode connected to the GPIO pin and the
# anode connected to a resistor and then to 3.3V
led1 = LED(17, active_high = False)
led2 = LED(27, active_high = False)

# Initalize the LED's to off and set the current state
# of the LED's in variables
led1.off()
led2.off()

# False indicates the LED is off and True indicates on
led1_state = False
led2_state = False

# Function to handle the event when button1 is pressed
def button1_pressed():
    global led1_state
    global led1
    if led1_state:
        led1.off()
        led1_state = False
    else:
        led1.on()
        led1_state = True
    

# Function to handle the event when button2 is pressed
def button2_pressed():
    global led2_state
    global led2
    if led2_state:
        led2.off()
        led2_state = False
    else:
        led2.on()
        led2_state = True


# Main Program
# The buttons are connected to GPIO pins
# GPIO 5 and GPIO 6 and then to ground
button1 = Button(5, pull_up = True)
button2 = Button(6, pull_up = True)

# Setup event handlers for when buttons are pressed 
button1.when_pressed = button1_pressed
button2.when_pressed = button2_pressed

# Main loop

while True:
    time.sleep(0.01)
    
