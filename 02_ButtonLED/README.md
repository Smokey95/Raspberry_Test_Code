# 02_ButtonLED #
A extenden version of the simple LED using a button as trigger
***
## Hardware Setup ##
Connect a LED and a 330Ω resistor like seen [here](https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins)<br>
Add a button to GPIO27 (Pin13)

***
## Execution ##
    $ python3 main.py

To terminate the execution use keyboard interrupts or hold the button for more then 5 seconds.