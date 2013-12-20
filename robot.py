import wpilib

import config
import utils
import common

from drive import Drive


class MyRobot(wpilib.SimpleRobot):
    def __init__(self):
        super().__init__()

        self.components = []

        self.drive = Drive(config.Drive)
        self.components.append(self.drive)

    def RobotInit(self):
        wpilib.Wait(0.25)

        for component in self.components:
            component.robot_init()

    def Disabled(self):
        dog = self.GetWatchdog()
        dog.SetEnabled(True)
        dog.SetExpiration(0.25)

        for componet in self.components:
            componet.disabled_init()

        while wpilib.IsDisabled():
            dog.Feed()

            for componet in self.components:
                componet.disabled_tick()

            wpilib.Wait(0.01)

    def Autonomous(self):
        dog = self.GetWatchdog()
        dog.SetEnabled(True)
        dog.SetExpiration(0.25)

        for componet in self.components:
#            componet.auto_init()

        while wpilib.IsAutonomous() and wpilib.IsEnabled():
            dog.Feed()

#            for componet in self.components:
#                componet.auto_tick()

            wpilib.Wait(0.01)

    def OperatorControl(self):
        dog = self.GetWatchdog()
        dog.SetEnabled(True)
        dog.SetExpiration(0.25)

        for componet in self.components:
            componet.op_init()

        while self.IsOperatorControl() and self.IsEnabled():
            dog.Feed()
            for componet in self.components:
                componet.op_tick()

            wpilib.Wait(0.01)


def run():
    robot = MyRobot()
    robot.StartCompetition()
