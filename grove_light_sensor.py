#!/usr/bin/env python
#
# GrovePi Example for using the Grove Light Sensor and the LED together to turn the LED On and OFF if the background light is greater than a threshold.
# Modules:
#   http://www.seeedstudio.com/wiki/Grove_-_Light_Sensor
#   http://www.seeedstudio.com/wiki/Grove_-_LED_Socket_Kit
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
#
# Have a question about this example?  Ask on the forums here:  http://forum.dexterindustries.com/c/grovepi
#
'''
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2017  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import time
import grovepi

# Connect the Grove Light Sensor to analog port A0
# SIG,NC,VCC,GND
light_sensor = 0

# Connect the LED to digital port D6
# SIG,NC,VCC,GND
blueLed = 6
redLed = 5
greenLed = 4

# Turn on LED once sensor exceeds threshold resistance
threshold = 75

grovepi.pinMode(light_sensor,"INPUT")
grovepi.pinMode(blueLed,"OUTPUT")
grovepi.pinMode(redLed,"OUTPUT")
grovepi.pinMode(greenLed,"OUTPUT")

while True:
    try:
        # Get sensor value
        sensor_value = grovepi.analogRead(light_sensor)

        # Calculate resistance of sensor in K
        resistance = (float)(1023 - sensor_value) * 10 / sensor_value

        #turn on blue LED
        if resistance > 90 and resistance < 100:
            # Send HIGH to switch on LED
            grovepi.digitalWrite(blueLed,1)
        else:
            # Send LOW to switch off LED
            grovepi.digitalWrite(blueLed,0)
        
        #turning on red LED
        if resistance > 75 and resistance < 90:
            # Send HIGH to switch on LED
            grovepi.digitalWrite(redLed,1)
        else:
            # Send LOW to switch off LED
            grovepi.digitalWrite(redLed,0)
            
        #turn on green LED
        if resistance > 50 and resistance < 75:
            # Send HIGH to switch on LED
            grovepi.digitalWrite(greenLed,1)
        else:
            # Send LOW to switch off LED
            grovepi.digitalWrite(greenLed,0)
            
        #turn on blue and green LED  
        if resistance < 50:
            # Send HIGH to switch on LED
            grovepi.digitalWrite(blueLed,1)
            grovepi.digitalWrite(greenLed,1)
        else:
            # Send LOW to switch off LED
            grovepi.digitalWrite(blueLed,0)
            grovepi.digitalWrite(greenLed,0)

        print("sensor_value = %d resistance = %.2f" %(sensor_value,  resistance))
        time.sleep(.5)

    except IOError:
        print ("Error")
 