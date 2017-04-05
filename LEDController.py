import RPi.GPIO as GPIO
import Pyro4

def LEDController(self):

    def __init__(self):

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(3, GPIO.OUT)
        self.dutyCycle = 0
        self.p = GPIO.PWM(3, self.dutyCycle)
        self.p.start(self.dutyCycle)
    
    @Pyro4.expose
    def max(self):
        self.dutyCycle = 0
        self.p.ChangeDutyCycle(self.dutyCycle)
    
    @Pyro4.expose
    def min(self):
        self.dutyCycle = 0
        self.p.ChangeDutyCycle(self.dutyCycle)
        
    @Pyro4.expose
    def stepUp(self):
        self.dutyCycle += 10
        self.p.ChangeDutyCycle(self.dutyCycle)

    @Pyro4.expose
    def stepDown(self):
        self.dutyCycle -= 10
        self.p.ChangeDutyCycle(self.dutyCycle)
