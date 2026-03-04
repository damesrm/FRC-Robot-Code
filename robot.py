import wpilib
from drivetrain import Drivetrain
from intake import Intake
from shooter import Shooter

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        self.drivetrain = Drivetrain()
        self.intake = Intake()
        self.joystick = wpilib.Joystick(0)
        self.shooter = Shooter()

    def teleopPeriodic(self):
        self.drivetrain.arcade_drive(-self.joystick.getY(), self.joystick.getX())

        if self.joystick.getRawButton(1):
            self.intake.turnOn()
        elif self.joystick.getRawButton(2):
            self.intake.turnOff()
        elif self.joystick.getRawButton(3):
            self.intake.dropBall()
        else:
            self.intake.stop()

        if self.joystick.getRawButton(4):
            self.shooter.activate()         
        elif self.joystick.getRawButton(5):
            self.shooter.deactivate()
        elif self.joystick.getRawButton(6):
            self.shooter.setBySetpoint(5000)
        elif self.joystick.getRawButton(7):
            self.shooter.bangBangActivate(5000)
        else:
            self.shooter.deactivate()            