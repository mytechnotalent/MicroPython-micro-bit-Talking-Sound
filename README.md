![image](https://github.com/mytechnotalent/MicroPython-micro-bit-Talking-Sound/blob/main/MicroPython-micro-bit%20Talking%20Sound.png?raw=true)

# MicroPython-micro-bit
# Talking Sound
The micro:bit Talking LED Blink And Breath is a micro:bit Electronic Educational Engagement Tool designed to help students create a talking sound application.

## Schematic
![image](https://github.com/mytechnotalent/MicroPython-micro-bit-Talking-Sound/blob/main/schematic.png?raw=true)<br>
*** NOTE *** USE PIN1 INSTEAD OF PIN7 (GREEN WIRE)

## Parts
[micro:bit](https://microbit.org/buy/?location=US&version=microbitV2)<br>
[Ks0360 Keyestudio Sensor Shield V2 for BBC micro:bit](https://www.amazon.com/gp/product/B08H7VSLZH/)<br>
* Keyestudio Micro bit Sensor V2 Shield * 1
* keyestudio Digital Buzzer Module * 1
* Dupont jumper wire * 3

## STEP 1: Navigate To The FREE micro:bit Python Web Editor
[micro:bit Python Web Editor](https://python.microbit.org/v/beta)<br><br>
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_Blink_And_Breath/blob/main/STEP%201.png?raw=true)

## STEP 2: Plug micro:bit V2 Into Computer
***PLUG IN USB CABLE TO COMPUTER AND DEVICE**

## STEP 3: Click CONNECT
![image](https://github.com/mytechnotalent/MicroPython-micro-bit-Talking-Sound/blob/main/STEP%203.png?raw=true)

## STEP 4: Click "BBC micro:bit CMSIS-DAP" & CONNECT
![image](https://github.com/mytechnotalent/MicroPython-micro-bit-Talking-Sound/blob/main/STEP%204.png?raw=true)

## STEP 5: Highlight Sample Code - Select All
![image](https://github.com/mytechnotalent/MicroPython-micro-bit-Talking-Sound/blob/main/STEP%205.png?raw=true)

## STEP 6: Click Backspace On Keyboard To Delete Sample Code
![image](https://github.com/mytechnotalent/MicroPython-micro-bit-Talking-Sound/blob/main/STEP%206.png?raw=true)

## STEP 7: Copy Study Buddy Python Code Template Into Python Web Editor

# CODE
```python
from time import sleep_ms

from microbit import pin1, display, Image
from speech import say

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
```

## STEP 8: Rename Script Name To talking_blink_and_breath

## STEP 9: Click Save
![image](https://github.com/mytechnotalent/MicroPython-micro-bit-Talking-Sound/blob/main/STEP%209.png?raw=true)

## STEP 10: Click Download Python Script
![image](https://github.com/mytechnotalent/MicroPython-micro-bit-Talking-Sound/blob/main/STEP%2010.png?raw=true)

## STEP 11: Click Flash
![image](https://github.com/mytechnotalent/MicroPython-micro-bit-Talking-Sound/blob/main/STEP%2011.png?raw=true)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)
