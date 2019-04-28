from gpiozero import Button
from signal import pause
import os

# GPIO pin used for shutdown button
gpioShutdown = 24

# how long button should be pressed (seconds)
pressTime = 1

# script to run
def shutdown():
    os.system("sudo shutdown -h now")

#create button with parameters defined above
btn = Button(gpioShutdown, hold_time=pressTime)
btn.when_held = shutdown

#put this script in the background
pause()