import common

class Button(object):

    def __init__(self, joystick, buttonNumber):
        self.joy = joystick
        self.button = buttonNumber

    def get(self):
        return self.joy.GetRawButton(self.button)
