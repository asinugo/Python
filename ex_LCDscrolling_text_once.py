# Example program will slides text onto the screen from right to left once,
# then stops and leaves a cleared screen.
# Spring 2020

import I2C_LCD_driver
from time import *

thelcd = I2C_LCD_driver.lcd()

str_pad = " " * 16
my_long_string = "This is a string that needs to scroll"
my_long_string = str_pad + my_long_string

for i in range (0, len(my_long_string)):
    lcd_text = my_long_string[i:(i+16)]
    thelcd.lcd_display_string(lcd_text,1)
    sleep(0.4)
    thelcd.lcd_display_string(str_pad,1)
