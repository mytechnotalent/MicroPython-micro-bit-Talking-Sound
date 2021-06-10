from time import sleep_ms

from microbit import pin1, display, Image
from speech import say

# Customize bot speaking speed
SPEED = 95

while True:
    display.show(Image.SURPRISED)
    say('Sound On', speed=SPEED)
    pin1.write_digital(1)
    display.show(Image.HAPPY)
    sleep_ms(1000)
    display.show(Image.SURPRISED)
    say('Sound Off', speed=SPEED)
    display.show(Image.HAPPY)
    pin1.write_digital(0)
    sleep_ms(1000)
