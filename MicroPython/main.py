"""
Created by: Elliott
Created on: Sep 2024
This module is a Micro:bit MicroPython program takes tempitur and converts to kelven
"""

from microbit import *

temperature = 0

display.clear()
sleep(1000)

while True:
    if button_a.is_pressed():
        temperature = temperature + input.temperature()
        temperature = round
        display.scroll("the temperature is:")
        display.show(temperature)
        display.scroll("K.")
        display.show(Image.HAPPY)
