import time

from machine import Pin
from motor_control import MotorControl

MOTOR_ENABLE_PIN1 = 13
MOTOR_ENABLE_PIN2 = 27
MOTOR_PWM_PIN1 = 12
MOTOR_PWM_PIN2 = 33

e1Pin = Pin(MOTOR_ENABLE_PIN1, Pin.OUT, Pin.PULL_DOWN) #E1
m1Pin = Pin(MOTOR_PWM_PIN1, Pin.OUT, Pin.PULL_DOWN) #M1
e2Pin = Pin(MOTOR_ENABLE_PIN2, Pin.OUT, Pin.PULL_DOWN) #E2
m2Pin = Pin(MOTOR_PWM_PIN2, Pin.OUT, Pin.PULL_DOWN) #M2

motorControl = MotorControl(e1Pin, m1Pin, e2Pin, m2Pin)

motorControl.stop()
time.sleep(6)
motorControl.rotateInPlace(50, MotorControl.DIRECTION_RIGHT)
time.sleep(6)
motorControl.forward(45, MotorControl.DIRECTION_BACK)
time.sleep(6)
motorControl.stop()


