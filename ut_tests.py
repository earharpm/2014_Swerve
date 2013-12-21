import unittest

import utils
import mock

import drive


def seq(start, stop, step=1):
    n = int(round((stop - start)/float(step)))
    if n > 1:
        return([start + step*i for i in range(n+1)])
    else:
        return([])


class TestDrive(unittest.TestCase):

    def setUp(self):
        self.joystick = mock.Joystick()
        self.drive_motors = [ mock.Motor() for x in range(5)]
        self.steering_motors = [ mock.Motor() for x in range(5)]
        self.encoder = mock.Encoder()
        self.hs_button = mock.Button()
        self.hs_steer_button = mock.Button()

        class MockDriveConfig(object):
            # Motors & Drive System
            drive_joy = self.joystick

            drive_motors = self.drive_motors
            steering_motors = self.steering_motors
            encoder = self.encoder

            hs_button = self.hs_button
            hs_steer_button = self.hs_steer_button

        self.drive = drive.Drive(MockDriveConfig)

    def tearDown(self):
        pass

    def test_throttle(self):
        self.joystick.x = 0.0

        # Sweep forward
        for mag in seq(-1.0, 1.0, 0.1):
            self.joystick.magnitude = mag

            self.drive.op_tick()

            for i in self.drive.drive_motors:
                self.assertEquals(i.speed, self.joystick.magnitude)

        # Sweep back
        for mag in seq(1.0, -1.0, -0.1):
            self.joystick.magnitude = mag

            self.drive.op_tick()

            for i in self.drive.drive_motors:
                self.assertEquals(i.speed, self.joystick.magnitude)

### NEEDS WORK ###
    # This one is broken and I really don't want to think about it....
    def test_steering(self):
        self.joystick.y = 0.0

        # Sweep forward
        for x in seq(-1.0, 1.0, 0.1):
            self.joystick.x = x

            self.drive.op_tick()

            self.assertEquals(self.robot_drive.speed, self.joystick.y)
            self.assertEquals(self.robot_drive.rotation, self.joystick.x)

        # Sweep back
        for x in seq(1.0, -1.0, -0.1):
            self.joystick.x = x

            self.drive.op_tick()

            self.assertEquals(self.robot_drive.speed, self.joystick.y)
            self.assertEquals(self.robot_drive.rotation, self.joystick.x)

# These should work though
    def test_steering_limits(self):
        # CCW Limits
        self.encoder.count = -100

        for x in range(-180, 180):
            self.joystick.dir = x

            drive.op_tick()

            for i in self.drive.steering_motors:
                if i.speed < 0
                    self.fail()

        # CW Limits
        self.encoder.count = 100

        for x in range(-180, 180):
            self.joystick.dir = x

            drive.op_tick()

            for i in self.drive.steering_motors:
                if i.speed > 0
                    self.fail()


    def test_half_speed_drive_throttle(self):
        self.hs_button.pressed = True
        self.hs_steer_button.pressed = False

        # Sweep forward
        for mag in seq(-1.0, 1.0, 0.1):
            self.joystick.magnitude = mag

            self.drive.op_tick()

            for i in self.drive.drive_motors:
                self.assertEquals(i.speed = self.joystick.magnitude/2)

        # Sweep back
        for mag in seq(1.0, -1.0, -0.1):
            self.joystick.magnitude = mag

            self.drive.op_tick()

            for i in self.drive.drive_motors:
                self.assertEquals(i.speed = self.joystick.magnitude/2)

    def test_half_speed_turn_throttle():
        self.hs_button.pressed = False
        self.hs_steer_button.pressed = True

        # Sweep forward
        for mag in seq(-1.0, 1.0, 0.1):
            self.joystick.magnitude = mag

            self.drive.op_tick()

            for i in self.drive.drive_motors:
                self.assertEquals(i.speed = self.joystick.magnitude/2)

            for i in self.drive.steering_motors:
                if i.speed > .5:
                    self.fail()
                elif i.speed < -.5:
                    self.fail()

        # Sweep back
        for mag in seq(1.0, -1.0, -0.1):
            self.joystick.magnitude = mag

            self.drive.op_tick()

            for i in self.drive.drive_motors:
                self.assertEquals(i.speed = self.joystick.magnitude/2)

            for i in self.steering_motors:
                if i.speed > .5:
                    self.fail()
                elif i.speed < -.5:
                    self.fail()
