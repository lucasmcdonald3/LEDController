# A simple program to show off the utility and ease of use of HomeRemote.
# Uses HomeRemote's stepper remote to control an LED.
# The stepper remote has controls for incrementing, maximizing, and minimizing a value.
# For this program, the value being controlled is the duty cycle of the PWM lighting the LED.

import RPi.GPIO as GPIO

class LEDController():

    def __init__(self):
        
        # set up the pins on the RPi
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(3, GPIO.OUT)
        
        # open the text file with the duty cycle
        self.file = open("dutyCycle.txt", "r")
        
        # set the duty cycle to the stored value
        self.dutyCycle = int(self.file.read())
        
        # start the PWM with the duty cycle
        self.p = GPIO.PWM(3, self.dutyCycle)
        self.p.start(self.dutyCycle)

	self.file = open("dutyCycle.txt", "w")
    
    # sets duty cycle to 100
    def max(self):
        self.dutyCycle = 100
        self.p.ChangeDutyCycle(self.dutyCycle)
        self.file.write(str(self.dutyCycle))
    
    # sets duty cycle to 0
    def min(self):
        self.dutyCycle = 0
        self.p.ChangeDutyCycle(self.dutyCycle)
        self.file.write(str(self.dutyCycle))
        
    # increases duty cycle by 10
    def stepUp(self):
        if(self.dutyCycle < 100):
            self.dutyCycle += 10
            self.p.ChangeDutyCycle(self.dutyCycle)
            self.file.write(str(self.dutyCycle))

    # decreases duty cycle by 10
    def stepDown(self):
        if(self.dutyCycle > 0):
            self.dutyCycle -= 10
            self.p.ChangeDutyCycle(self.dutyCycle)
            self.file.write(str(self.dutyCycle))
