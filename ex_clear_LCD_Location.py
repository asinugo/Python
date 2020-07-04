# Example to write to the LCD Display and clear the screen
# Spring 2020

import I2C_LCD_driver
from time import *

thelcd = I2C_LCD_driver.lcd()

thelcd.lcd_display_string("Hello World!", 1)
sleep(1)

thelcd.lcd_clear()

