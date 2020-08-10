import grovepi
import math
from grove_rgb_lcd import *
import json
import time

# Connect the Grove Temperature & Humidity Sensor Pro to digital port D7
sensor = 7

# Connect the Grove Light Sensor to analog port A0
light_sensor = 0

# Connect the LED to digital ports D4, D5, D6
blueLed = 4
redLed = 5
greenLed = 6

# threshold for light sensor
threshold = 100

blue = 0
white = 1

grovepi.pinMode(light_sensor,"INPUT")
grovepi.pinMode(blueLed,"OUTPUT")
grovepi.pinMode(redLed,"OUTPUT")
grovepi.pinMode(greenLed,"OUTPUT")

temp = "temp"
humidity = "humidity"


# Creating the JSOn file and the data
def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

while True:
    try:

        data={"weather":[]}
        data["weather"].append({"temp":temp,"humidity":humidity})
        
        sensor_value = grovepi.analogRead(light_sensor)
        [temp,humidity] = grovepi.dht(sensor,blue)
                
        resistance = (float)(1023 - sensor_value) * 10 / sensor_value
                
        if resistance > threshold:
            print("Waiting till daylight")
                    
        elif math.isnan(temp) == False and math.isnan(humidity) == False:
            #convert C to F
            temp = (temp * (9/5)) + 32
            print("temp = %.02fF humidity =%.02f%%"%(temp, humidity))
            
        #Turning on Green LED
        if temp > 60 and temp < 85 and humidity < 80:
            grovepi.digitalWrite(greenLed,1)
            print("Green LED ON")
            time.sleep(5)
        else:
            grovepi.digitalWrite(greenLed,0)

        #Turning on Blue LED
        if temp > 85 and temp < 95 and humidity < 80:
            grovepi. digitalWrite(blueLed,1)
            print("Blue LED ON")
            time.sleep(5)
        else:
            grovepi.digitalWrite(blueLed,0)
         
        #Turning on Red LED
        if temp > 95:
            grovepi.digitalWrite(redLed,1)
            print("Red LED ON")
            time.sleep(5)
        else:
            grovepi.digitalWrite(redLed,0)

        #Turning on Green and Blue LEDs
        if humidity > 80:
            grovepi.digitalWrite(greenLed,1)
            grovepi.digitalWrite(blueLed,1)
            print("Green and Blue LEDs ON")
            time.sleep(5)
        else:
            grovepi.digitalWrite(greenLed,0)
            grovepi.digitalWrite(blueLed,0)

            #write data to JSON File
            writeToJSONFile('./','data',data)
            
            time.sleep(1800)
            
    except IOError:
        print ("Error") 
        
    
    

         