import sys
import Adafruit_DHT

from time import sleep

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
    sleep(5)