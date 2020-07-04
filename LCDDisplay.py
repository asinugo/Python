#Chinedu Asinugo 
#Lab 7- CIT 394
#Professor Ken Roth

#Part 1 
#program to display that LCD is working
#Import lcd driver and time
import I2C_LCD_driver
import time
#Outputting Hello World to the LCD
thelcd = I2C_LCD_driver.lcd()
thelcd.lcd_display_string("Hello World!",1, 1)
#Sleep for 10 seconds then clear
time.sleep(10)
thelcd.lcd_clear()

#part 2
#program to read the values from channel 0 through channel three and display the values on the LCD
from gpiozero import MCP3208
import I2C_LCD_driver
import time
 
#Defining the channels to be used
ch0 = MCP3208(channel = 0, differential = False, max_voltage = 3.3)
ch1 = MCP3208(channel = 1, differential = False, max_voltage = 3.3)
ch2 = MCP3208(channel = 2, differential = False, max_voltage = 3.3)
ch3 = MCP3208(channel = 3, differential = False, max_voltage = 3.3)
 
thelcd = I2C_LCD_driver.lcd()
while True:
# Define Celcius/Farenheit
Celcius = round(ch3.voltage * 100, 1)
Ferenheit = round((Celcius * 9/5) + 32, 1)
#commented out code(code to test the MCP3208)
#print("The temperature is %6.2f C." % Celcius)
#print("The temperature is %6.2f F." % Ferenheit)
thelcd.lcd_display_string("Ch0 Raw:" +str(ch0.raw_value)+str("V"))
thelcd.lcd_display_string(str(Celcius)+"C | "+str(Ferenheit)+"F",2,0)
time.sleep(5)
thelcd.lcd_clear()
thelcd.lcd_display_string("Ch0 Value:" +str(ch0.value)+str("V"))
thelcd.lcd_display_string(str(Celcius)+"C | "+str(Ferenheit)+"F",2,0)
time.sleep(5)
thelcd.lcd_clear()
thelcd.lcd_display_string("Ch0 Voltage:" +str(ch0.voltage)+str("V"))
thelcd.lcd_display_string(str(Celcius)+"C | "+str(Ferenheit)+"F",2,0)
time.sleep(5)
thelcd.lcd_clear()
thelcd.lcd_display_string("Ch1 Raw:" +str(ch1.raw_value)+str("V"))
thelcd.lcd_display_string(str(Celcius)+"C | "+str(Ferenheit)+"F",2,0)
time.sleep(5)
thelcd.lcd_clear()
thelcd.lcd_display_string("Ch1 Value:" +str(ch1.value)+str("V"))
thelcd.lcd_display_string(str(Celcius)+"C | "+str(Ferenheit)+"F",2,0)
time.sleep(5)
thelcd.lcd_clear()
thelcd.lcd_display_string("Ch1 Voltage:" +str(ch1.voltage)+str("V"))
thelcd.lcd_display_string(str(Celcius)+"C | "+str(Ferenheit)+"F",2,0)
time.sleep(5)
thelcd.lcd_clear()
thelcd.lcd_display_string("Ch2 Raw:" +str(ch2.raw_value)+str("V"))
thelcd.lcd_display_string(str(Celcius)+"C | "+str(Ferenheit)+"F",2,0)
time.sleep(5)
thelcd.lcd_clear()
thelcd.lcd_display_string("Ch2 Value:" +str(ch2.value)+str("V"))
thelcd.lcd_display_string(str(Celcius)+"C | "+str(Ferenheit)+"F",2,0)
time.sleep(5)
thelcd.lcd_clear()
thelcd.lcd_display_string("Ch2 Voltage:" +str(ch2.voltage)+str("V"))
thelcd.lcd_display_string(str(Celcius)+"C | "+str(Ferenheit)+"F",2,0)
time.sleep(5)
thelcd.lcd_clear()
thelcd.lcd_display_string("Ch3 Raw:" +str(ch3.raw_value)+str("V"))
thelcd.lcd_display_string(str(Celcius)+"C | "+str(Ferenheit)+"F",2,0)
time.sleep(5)
thelcd.lcd_clear()
thelcd.lcd_display_string("Ch3 Value:" +str(ch3.value)+str("V"))
thelcd.lcd_display_string(str(Celcius)+"C | "+str(Ferenheit)+"F",2,0)
time.sleep(5)
thelcd.lcd_clear()
thelcd.lcd_display_string("Ch3 Voltage:" +str(ch3.voltage)+"V")
thelcd.lcd_display_string(str(Celcius)+"C | "+str(Ferenheit)+"F",2,0)
time.sleep(5)
thelcd.lcd_clear()
