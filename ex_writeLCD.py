# Example to write to the LCD Display
# Spring 2020

import I2C_LCD_driver
from time import *

thelcd = I2C_LCD_driver.lcd()

thelcd.lcd_display_string("Hello World!", 1)
