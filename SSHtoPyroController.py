# This file converts the SSH command sent to the device into usable data for the Raspberry Pi.
# The name cannot be changed as it is explicitly defined in the HomeRemote app.
# Also, the "if(arg == "max")" statements have explicitly defined test strings (max, min, stepUp, stepDown).
# These are explicitly defined in the HomeRemote app and should not be modified.
# However, anything else can be modified. HomeRemote simply provides a platform to execute your own code from a remote.

import sys
import time
from LEDController import LEDController

# LEDController uses the Stepper Remote, which takes in one argument.
arg = sys.argv[1]

# Create the LEDController object that will manage the LED.
ledObject = LEDController()

# Based on the argument in the command, tell the LEDController to do something.
# You CANNOT change the equality tests in the if statement.
# The test strings are explicitly defined in the HomeRemote app and cannot be modified.
if(arg == "max"):
    ledObject.max()
elif(arg == "min"):
    proxymotor.min()
elif(arg == "stepUp"):
    print(proxymotor.inchesMotorMover(float(arg1), float(arg2)))
elif(arg == "stepDown"):
    print(proxymotor.radecScan(float(arg1), float(arg2)))
exit()
