import RPi.GPIO as GPIO
from time import sleep

LED = 12
BUTTON = 13

GPIO.setmode(GPIO.BOARD)                        #setting numbering of GPIO pins by BOARD format
GPIO.setwarnings(False)                         #disable warings

GPIO.setup(LED,GPIO.OUT,initial=GPIO.LOW)       #setting up pin 12 as output with initial pin status as off or LOW
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)                     #setting up pin 13 as input

#-----------------------------------------------main
print("Started")

breakcount = 0

while(True):
    
    if not GPIO.input(BUTTON):
        GPIO.output(LED, GPIO.HIGH)
        breakcount += 1
    else:
        GPIO.output(LED, GPIO.LOW)
        breakcount = 0
    
    if breakcount == 25:
        break

    sleep(0.2)

print("Stopped")
GPIO.output(LED, GPIO.LOW)