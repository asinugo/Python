# Example to write to the LCD Display to display Blinking Text
# To make text blink we need to display it wait a period of
# time then clear the screen. We do this over and over.
# Spring 2020

import time
import I2C_LCD_driver
thelcd = I2C_LCD_driver.lcd()

while True:
    thelcd.lcd_display_string("Hello world!", 1)
    time.sleep(1)
    thelcd.lcd_clear()
    time.sleep(1)

