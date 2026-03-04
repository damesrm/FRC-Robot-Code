import wpilib
import rev
import wpimath.controller

class Intake:
    def __init__(self):
        self.arm_motor = rev.SparkMax(50, rev.SparkLowLevel.MotorType.kBrushless)
        self.roller_motor = rev.SparkMax(51, rev.SparkLowLevel.MotorType.kBrushless)
        self.encoder = self.arm_motor.getEncoder()

        self.arm_pid = wpimath.controller.PIDController(0.006, 0.0, 0.0)
        self.arm_pid.setTolerance(0.1)
        self.encoder.setPosition(0)

    def get_posicao_graus(self):
        return (self.encoder.getPosition())

    def turnOn(self):
        self.roller_motor.set(0.8) 
        setpoint = 70 
        posicao_atual = (self.encoder.getPosition() / 2.87) * 360
      
        output = self.arm_pid.calculate(posicao_atual, setpoint)
        
        output = max(min(output, 0.4), -0.4) 

        if not self.arm_pid.atSetpoint():
            self.arm_motor.set(output)
        else:
            self.arm_motor.set(0)
        
        print(f"Graus: {posicao_atual:.2f} | Out: {output:.2f}")

    def turnOff(self):
        self.roller_motor.set(0)
        setpoint = 0  
        posicao_atual = (self.encoder.getPosition() / 2.87) * 360

        output = self.arm_pid.calculate(posicao_atual, setpoint)

        output = max(min(output, 0.4), -0.4) 

        if not self.arm_pid.atSetpoint():
            self.arm_motor.set(output)
        else:
            self.arm_motor.set(0)
        
        print(f"Graus: {posicao_atual:.2f} | Out: {output:.2f}")

    def dropBall(self):
        self.roller_motor.set(-0.8) 
        setpoint = 70 
        posicao_atual = (self.encoder.getPosition() / 2.87) * 360
      
        output = self.arm_pid.calculate(posicao_atual, setpoint)
        
        output = max(min(output, 0.4), -0.4) 

        if not self.arm_pid.atSetpoint():
            self.arm_motor.set(output)
        else:
            self.arm_motor.set(0)
        
        print(f"Graus: {posicao_atual:.2f} | Out: {output:.2f}")