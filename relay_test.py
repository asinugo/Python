# This program turns a relay on that is connected to GPIO5
# Remember with a relay we need to have a fly wheel diode
# to protect the Raspberry Pi
# We will use the LED from GPIOZERO to control the relay

from gpiozero import LED
from time import sleep

# The way we have the relay wired it will turn on when the GPIO pin is taken high
# so we don't need to change any of the defaults
relay = LED(5)

for i in range(0,5):
	relay.on()
	sleep(5)
	relay.off()
	sleep(5)
