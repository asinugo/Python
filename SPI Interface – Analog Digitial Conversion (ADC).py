#Chinedu Asinugo 
#Lab 6- CIT 394
#Professor Ken Roth
#program to make use of the SPI interface, MCP3208 ADC and the LM35 temperature sensor to measure analog values

#Import required modules
from gpiozero import MCP3208
import time
#Defining the channels to be used
ch0 = MCP3208(channel = 0, differential = False, max_voltage = 3.3)
ch1 = MCP3208(channel = 1, differential = False, max_voltage = 3.3)
ch2 = MCP3208(channel = 2, differential = False, max_voltage = 3.3)
ch3 = MCP3208(channel = 3, differential = False, max_voltage = 3.3)

#Main Loop
while True:
#Assign the raw_value, value and voltage for each channel
ch0raw = ch0.raw_value
ch0val = ch0.value
ch0vol = ch0.voltage
ch1raw = ch1.raw_value
ch1val = ch1.value
ch1vol = ch1.voltage
ch2raw = ch2.raw_value
ch2val = ch2.value
ch2vol = ch2.voltage
ch3raw = ch3.raw_value
ch3val = ch3.value
ch3vol = ch3.voltage

#Ouput the raw_value, value and voltage for each channel
print("| CH 0 | RAW: %7.2f | VALUE: %7.2f | VOLTAGE: %7.2f |" % (ch0raw, ch0val, ch0vol))
print("| CH 1 | RAW: %7.2f | VALUE: %7.2f | VOLTAGE: %7.2f |" % (ch1raw, ch1val, ch2vol))
print("| CH 2 | RAW: %7.2f | VALUE: %7.2f | VOLTAGE: %7.2f |" % (ch2raw, ch2val, ch2vol))
print("| CH 3 | RAW: %7.2f | VALUE: %7.2f | VOLTAGE: %7.2f |" % (ch3raw, ch3val, ch3vol))
print("")
Cel = ch3vol * 100
Fer = (Cel * 9/5) + 32
print("The temperature is %6.2f C." % Cel)
print("The temperature is %6.2f F." % Fer)
#Wait 5 seconds and run it again
time.sleep(5)
