# Example to write to the LCD Display at a specific location
# Spring 2020

import I2C_LCD_driver
from time import *

thelcd = I2C_LCD_driver.lcd()

# Output to row 2 and starting in column 3
thelcd.lcd_display_string("Hello World!", 2, 3) 
