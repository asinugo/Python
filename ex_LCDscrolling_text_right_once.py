# Example program scrolls text onto the screen from left to right once,
# then stops and leaves the first 16 characters of the text string on
# the screen
# Spring 2020

import I2C_LCD_driver
from time import *

thelcd = I2C_LCD_driver.lcd()

padding = " " * 16
my_long_string = "This is a string that needs to scroll"
padded_string = my_long_string + padding

for i in range (0, len(my_long_string)):
    lcd_text = padded_string[((len(my_long_string)-1)-i):-i]
    thelcd.lcd_display_string(lcd_text,1)
    sleep(0.4)
    thelcd.lcd_display_string(padding[(15+i):i], 1)
 
