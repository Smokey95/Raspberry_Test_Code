import RPi.GPIO as GPIO
from time import sleep

SWITCH = 12

GPIO.setmode(GPIO.BOARD)                                    #setting numbering of GPIO pins by BOARD format
GPIO.setwarnings(False)                                     #disable warings

GPIO.setup(SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)     #setting up 12 13 as input

#-----------------------------------------------main
print("Started")


while(True):
    
    if not GPIO.input(SWITCH):
        print("SWITCH OPENED")
    else:
        print("SWITCH CLOSED")

    sleep(0.2)