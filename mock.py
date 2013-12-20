class Button(object):

    def __init__(self):
        self.pressed = False

    def get(self):
        return self.pressed


class Joystick(object):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.magnitude = 0
        self.dir = 0

    def GetX(self):
        return self.x

    def GetY(self):
        return self.y

    def GetMagnitude(self):
        return self.magnitude

    def GetDirectionDegrees(self):
        return self.dir


class Motor(object):

    def __init__(self):
        self.speed = 0

    def Set(self, speed):
        self.speed = speed

    def Get(self):
        return self.speed


class encoder(object):

    def __init__(self):
        self.count = 0

    def Start():
        pass

    def Get(self):
        return self.count
