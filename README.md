# 🏎️ FRC Robot Control System (Python)

## 📌 Overview

This project is a Python-based control system for an FRC-style robot built using WPILib and the REV SparkMax API.

It demonstrates real-world robotics concepts such as motor control, encoder feedback, PID control loops, Bang-Bang control, and object-oriented design.

The robot includes:

- Differential drivetrain  
- Intake mechanism with PID-controlled arm  
- Shooter system with manual, PID, and Bang-Bang control  

---

## ⚙️ Technologies Used

- Python  
- WPILib (RobotPy)  
- REV SparkMax API  
- WPIMath (PIDController, BangBangController)  
- TimedRobot framework  

---

## 🧠 Architecture

The system is organized using separate classes for each subsystem:

### Drivetrain
Handles robot movement using a DifferentialDrive configuration with four brushless motors.

### Intake
Controls:
- Roller motor (ball intake/outtake)
- Arm positioning using encoder feedback and PID control

### Shooter
Controls a flywheel motor using:
- Direct power control
- PID closed-loop control
- Bang-Bang control strategy

The main robot logic is implemented using `wpilib.TimedRobot`.

---

## 🎮 Controls

Joystick axes:
- Y-axis → Forward / backward
- X-axis → Rotation (arcade drive)

Buttons:
- Button 1 → Intake ON  
- Button 2 → Intake OFF  
- Button 3 → Drop Ball  
- Button 4 → Shooter manual activation  
- Button 5 → Shooter stop  
- Button 6 → Shooter PID setpoint control  
- Button 7 → Shooter Bang-Bang control  

---

## 🔍 Concepts Demonstrated

- Object-Oriented Programming  
- Motor configuration with SparkMax  
- Encoder-based feedback  
- PID control loops  
- Bang-Bang control  
- Differential drive system  
- Real-time robot control structure  

---

## 🚀 How to Run

1. Install RobotPy / WPILib environment  
2. Connect to an FRC-compatible robot or simulation  
3. Deploy and run:

```bash
python robot.py
```

---

## 📚 Purpose

This project was developed to strengthen knowledge in robotics software engineering, control systems, and structured robot architecture using Python.