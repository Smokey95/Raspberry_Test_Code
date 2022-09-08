import RPi.GPIO as GPIO
from time import sleep

LED_RED = 11
LED_YEL = 13
LED_GRE = 15

GPIO.setmode(GPIO.BOARD)                        #setting numbering of GPIO pins by BOARD format
GPIO.setwarnings(False)                         #disable warings

GPIO.setup(LED_RED,GPIO.OUT,initial=GPIO.HIGH)       #setting up pin 12 as output with initial pin status as off or LOW
GPIO.setup(LED_YEL,GPIO.OUT,initial=GPIO.LOW)       #setting up pin 12 as output with initial pin status as off or LOW 
GPIO.setup(LED_GRE,GPIO.OUT,initial=GPIO.LOW)       #setting up pin 12 as output with initial pin status as off or LOW  

#-----------------------------------------------main
while(True):
    sleep(5)
    GPIO.output(LED_YEL, GPIO.HIGH)
    sleep(1)
    GPIO.output(LED_RED, GPIO.LOW)
    GPIO.output(LED_YEL, GPIO.LOW)
    GPIO.output(LED_GRE, GPIO.HIGH)
    sleep(5)
    GPIO.output(LED_YEL, GPIO.HIGH)
    GPIO.output(LED_GRE, GPIO.LOW)
    sleep(1)
    GPIO.output(LED_RED, GPIO.HIGH)
    GPIO.output(LED_YEL, GPIO.LOW)