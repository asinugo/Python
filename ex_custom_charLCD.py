# This example generates a custom "<" character
# You can create any pattern you want and print it to the display as a
# custom character. Each character is an array of 5 x 8 pixels.
# Up to 8 custom characters can be defined and stored in the LCD’s memory.
# Spring 2020

import I2C_LCD_driver
from time import *

thelcd = I2C_LCD_driver.lcd()

fontdata1 = [      
        [ 0b00010, 
          0b00100, 
          0b01000, 
          0b10000, 
          0b01000, 
          0b00100, 
          0b00010, 
          0b00000 ],
]

thelcd.lcd_load_custom_chars(fontdata1)
thelcd.lcd_write(0x80)
thelcd.lcd_write_char(0)

