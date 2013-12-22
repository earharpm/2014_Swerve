import wpilib
from utils import Button

# Joysticks
leftJoy = wpilib.Joystick(1)
rightJoy = wpilib.Joystick(2)


class Drive(object):
	has_gyro = False

    drive_joy = leftJoy

    drive_motors = [ wpilib.Jaguar(x*2) for x in range(5) ]
    steering_motors = [ wpilib.Jaguar(x*2 + 1) for x in range(5) ]
    encoder = wpilib.Encoder(1, 2)

    # Buttons
    hs_button = Button(leftJoy, 1)
    hs_steer_button = Button(leftJoy, 2)

# Core Functions
def CheckRestart():
    return
    # We need to do something about this at some point.....
