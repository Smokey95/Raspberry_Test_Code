import RPi.GPIO as GPIO
from time import sleep

LED = 12

GPIO.setmode(GPIO.BOARD)                        #setting numbering of GPIO pins by BOARD format
GPIO.setwarnings(False)                         #disable warings
GPIO.setup(LED,GPIO.OUT,initial=GPIO.LOW)       #setting up pin 12 as output with initial pin status as off or LOW 

#-----------------------------------------------main
print("Turn on LED")
GPIO.output(LED, GPIO.HIGH)
sleep(5)
print("Turn off LED")
GPIO.output(LED, GPIO.LOW)