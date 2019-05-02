from gpiozero import Button, LED
from signal import pause
import os

# GPIO pin used for shutdown button
gpioShutdown = 24

# GPIO pin used for LEDs
gpioGreenLED = 21
gpioYellowLED = 20
gpioRedLED = 16

# how long button should be pressed (seconds)
pressTime = 1

# script to run
def shutdown():
    green.on()
    yellow.on()
    red.on()
    os.system("sudo shutdown -h now")

# you probably don't need to change any code below this line

# create LEDs with parameters defined in io-config
green = LED(gpioGreenLED)
yellow = LED(gpioYellowLED)
red = LED(gpioRedLED)

# create button with parameters defined above & in io-config
btn = Button(gpioShutdown, hold_time=pressTime)
btn.when_held = shutdown

#put this script in the background
pause()