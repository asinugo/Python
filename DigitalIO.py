Part 2:
#Chinedu Asinugo

#Lab 4 & 5- Cit 394

#Professor Ken Roth

#test program for the reed switch,LEDs and the push button to verify their operation

# Import the required modules

from gpiozero import Button

from gpiozero import LED

import time



# Initialize buttons and LEDs

# Buttons are connected on GPIO 17 and GPIO 20

button1 = Button(17,pull_up = True) #assigning button object

button2 = Button(20,pull_up = True) #assigning reed


#LEDs are connected on GPIO 19 and GPIO 26

led1 = LED(19, active_high = False) # assigning led object

led2 = LED(26, active_high = False) # assigning led object

count = 0


# set LEDs to an initial state of 'off'

led1.off()

led2.off()


# Setting the state to False to signify that they are off 

led1_state = False

led2_state = False


# Main Loop

while True:


        # Pressing button 1 to toggle state of led1

        if button1.value == 1:

                if led1_state:

                        led1.off()

                        led1_state = False

                else:

                        led1.on()

                        led1_state = True


        # Pressing button 2 to toggle state of led2

        if button2.value == 1:

                if led2_state:

                        led2.off()

                        led2_state = False

                else:

                        led2.on()

                        led2_state = True

        time.sleep(0.01)

 

Part 3:
#Chinedu Asinugo 
#Lab 4 & 5- Cit 394

#Professor Ken Roth

# Import the required modules

from gpiozero import Button

from gpiozero import LED

from gpiozero import MotionSensor

import time


#Intitialize states

alarmstate = False

armed = False

reedstate = False


#Assign leds & sensor

armled = LED(19, active_high = False) # assigning led GPIO 19

alarmled = LED(26, active_high = False) # assigning led GPIO 26

motion = MotionSensor(21)


# Initialize buttons and LEDs on GPIO 17 and GPIO 20

pushButton = Button(17,pull_up = True) #assigning button GPIO 17

reedSwitch = Button(20,pull_up = True) #assigning reed GPIO 20


# Set LEDs to off initially

armled.off()

alarmled.off()
 

# False indicates the LED is off and true indicates on

armled_state = False

alarmled_state = False


# Initialize the disarm

print("Alarm System disarmed.")


# Define motion detect

def motionDetect():

        global alarmstate

        global armed

        global alarmled

        if alarmstate == False and armed == True:

                alarmled.on()

                alarmstate = True


                print("Motion detected, Alarm System Activated!")

                text()


# Define system armed

def systemArm():

        global armed

        global alarmstate

        global armled

        global armledstate

        alarmstate = False


        if armed == False:

                armed = True

                armled.on()

                print("Armed")

        else:

                armed = False

                armled.off()

                print("Disarmed")


# Define the Reed Switch on and off

def reedSwitch():

        global alarmstate

        global armed

        if armed == True and alarmstate == False:

                alarmled.on()

                alarmled_state = True

                alarmstate = True

                print("Reed Switch Opened")

                text()

 


def text():

#Define the email text message and text to my phone

        import smtplib

        import subprocess

        import urllib.request

        import time

        gmail_user = "lifeofaraspberrypi@gmail.com"

        gmail_password = "toorcit394toor"

        to = ["5714666297@tmomail.net"] #carrier's information

        subject = "Here's a text about the alarm"

        tostr = ", ".join(to)

        sent_from = gmail_user

        body = "Alert Alarm"

        email_text = """\

        From: %s

        To: %s

        Subject: %s

        %s


        """ % (sent_from, tostr, subject, body)


        try:

                server = smtplib.SMTP_SSL('smtp.gmail.com',465)

                server.ehlo()

                server.login(gmail_user, gmail_password)

                server.sendmail(sent_from, to, email_text)

                server.close()

                print("Email sent!")

        except:

                print("Email wasn't sent!")

#main function

while True:

# Define the motion sensor, button pressed, and reed swtich

        motion.when_motion = motionDetect

        pushButton.when_pressed = systemArm

        reedSwitch.when_released = reedSwitch

 

#When armed with no motion and reed switch

        if armed == True  and motion.value == 0 and reedSwitch.value == 1:

                alarmled.off()

                armledstate = False

                time.sleep(0.25)

                alarmstate = False