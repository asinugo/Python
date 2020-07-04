# Starting code for reading MCP3208 ADC
# Spring 2020

# Import required modules
from gpiozero import MCP3208
import time
import os

# Define the three channels we are using from the MCP3208

ch0 = MCP3208(channel=0, differential=False, max_voltage=3.3)
ch1 = MCP3208(channel=1, differential=False, max_voltage=3.3)
ch2 = MCP3208(channel=2, differential=False, max_voltage=3.3)

# Main Loop
while True:
# Output the raw_value, value and voltage for each channel
	time.sleep(5)
