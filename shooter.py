from rev import SparkMax, SparkLowLevel
from wpimath.controller import PIDController, BangBangController
from wpimath.units import rotationsPerMinuteToRadiansPerSecond


class Shooter:

    def __init__(self):
        self.flywheel = SparkMax(
            1, 
            SparkLowLevel.MotorType.kBrushless
        )

        self.encoder = self.flywheel.getEncoder()

        self.pid = PIDController(0.1, 0.0, 0.01) 
        self.bangbang = BangBangController()

    def activate(self):
        self.flywheel.set(0.7)

    def deactivate(self):
        self.flywheel.set(0)

    def setBySetpoint(self, setpoint):
        current = self.encoder.getPosition()
        output = self.pid.calculate(current, setpoint)
        self.flywheel.set(output)

    def bangBangActivate(self, rpm):
        setpoint = rotationsPerMinuteToRadiansPerSecond(rpm)
        current = self.encoder.getPosition()
        output = self.bangbang.calculate(current, setpoint)
        self.flywheel.set(output)