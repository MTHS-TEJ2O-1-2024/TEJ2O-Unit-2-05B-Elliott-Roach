"""
Created by: Elliott
Created on: Sep 2024
This module is a Micro:bit MicroPython program takes tempitur and converts to kelven
"""

from microbit import *

temp_k = 0

display.clear()
sleep(1000)

while True:
    if button_a.is_pressed():
        temp_k = temperature
        temp_k = str(temp_k + 273.15)
        temp_k = round
        display.scroll("the temperature is:")
        display.show(temp_k)
        display.scroll("K.")
        display.show(Image.HAPPY)
