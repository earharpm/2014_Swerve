import common


__all__ = ['Drive']


class Drive(common.ComponentBase):

    def __init__(self, config):
        self.drive_motors = config.drive_motors
        self.steering_motors = config.steering_motors
        self.encoder = config.encoder

        self.drive_joy = config.drive_joy
        self.hs_button = config.hs_button

        self.reversed = False

    def op_init(self):
        self.robot_drive.StopMotor()

    def op_tick(self):
        speed = self.drive_joy.GetMagnitude()
        angle = self.drive_joy.GetDirectionDegrees()

        pos = self.encoder.Get()

        if reversed:
            speed = -speed

        if angle > 180:
            angle -= 180
            self.reversed = not self.reversed

        if self.hs_button.get():
            speed /= 2

        for i in self.drive_motors:
            i.Set(speed)

        for i in self.steering_motors:
            i.Set(angle - pos / 180 + .1)
