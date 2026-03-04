import wpilib
import rev
import wpilib.drive

class Drivetrain:
    
    def __init__(self):
        self.front_left_motor = rev.SparkMax(52, rev.MotorType.kBrushless)
        self.front_right_motor = rev.SparkMax(53, rev.MotorType.kBrushless)
        self.back_left_motor = rev.SparkMax(54, rev.MotorType.kBrushless)
        self.back_right_motor = rev.SparkMax(55, rev.MotorType.kBrushless)

        self.left_motors = wpilib.SpeedControllerGroup(self.front_left_motor, self.back_left_motor)
        self.right_motors = wpilib.SpeedControllerGroup(self.front_right_motor, self.back_right_motor)

        self.drivetrain = wpilib.drive.DifferentialDrive(self.left_motors, self.right_motors)

        self.right_motors.setInverted(True)

    def arcade_drive(self, forward, rotation):
        self.drivetrain.arcadeDrive(forward, rotation)

