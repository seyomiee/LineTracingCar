# 02_ TurnModule.py
# =======================================================================
# 1)rightSwingTurn() and rightPointTurn()
# 2)leftPointTurn() and leftSwingTurn()
# =======================================================================
# student assignment (1) rightSwingTurn() v
# import GPIO  library
import RPi.GPIO as GPIO
from time import sleep
 
# set up GPIO mode as BOARD
GPIO.setmode(GPIO.BOARD)


# set GPIO warnings as false
GPIO.setwarnings(False)

# =======================================================================
# REVERSE function to control the direction of motor in reverse
def REVERSE(x):
   if x == 'True':
      return 'False'
   elif x == 'False':
      return 'True'
# =======================================================================

# =======================================================================
# Set the motor's true / false value to go forward.
forward0 = 'True'
forward1 = 'False'
# =======================================================================

# =======================================================================
#Set the motor's true / false value to the opposite.
backward0 = REVERSE(forward0)
backward1 = REVERSE(forward1)
# =======================================================================

# =======================================================================
# declare the pins of 12, 11, 35 in the Raspberry Pi
# as the left motor control pins in order to control left motor
# left motor needs three pins to be controlled

# (this codes includes
# the initialization the connection between left motor and Raspberry Pi)
# (this codes includes
# the connection between left motor and Raspberry Pi by software)
# =======================================================================
MotorLeft_A = 12
MotorLeft_B = 11
MotorLeft_PWM = 35

# =======================================================================
# declare the pins of 15, 13, 37 in the Raspberry Pi
# as the right motor control pins in order to control right motor
# right motor needs three pins to be controlled

# (this codes includes
# the initialization the connection between right motor and Raspberry Pi
# (this codes includes
# the connection between right motor and Raspberry Pi by software
# =======================================================================

MotorRight_A = 15
MotorRight_B = 13
MotorRight_PWM = 37


# ===========================================================================
# Control the DC motor to make it rotate clockwise, so the car will
# move forward.
# if you have different direction, you need to change HIGH to LOW
# or LOW to HIGH,in MotorLeft_A
# and LOW to HIGH or HIGH to LOW in MotorLeft_B
# if you have different direction, you need to change HIGH to LOW
# or LOW to HIGH in MotorLeft_A
# and LOW to HIGH or HIGH to LOW in MotorLeft_B
# ===========================================================================

def leftmotor(x):
	if x == 'True':
		GPIO.output(MotorLeft_A, GPIO.HIGH)
		GPIO.output(MotorLeft_B, GPIO.LOW)
	elif x == 'False':
		GPIO.output(MotorLeft_A, GPIO.LOW)
		GPIO.output(MotorLeft_B, GPIO.HIGH)
	else:
		print 'Config Error'

def rightmotor(x):
	if x == 'True':
		GPIO.output(MotorRight_A, GPIO.LOW)
		GPIO.output(MotorRight_B, GPIO.HIGH)
	elif x == 'False':
		GPIO.output(MotorRight_A, GPIO.HIGH)
		GPIO.output(MotorRight_B, GPIO.LOW)

# =======================================================================
# because the connections between motors (left motor) and Raspberry Pi will be
# established, the being connected GPIO pins of Raspberry Pi
# such as MotorLeft_A, MotorLeft_B, and MotorLeft_PWM
# should be clearly declared whether their roles of pins
# are output pin or input pin
# =======================================================================
GPIO.setup(MotorLeft_A,GPIO.OUT)
GPIO.setup(MotorLeft_B,GPIO.OUT)
GPIO.setup(MotorLeft_PWM,GPIO.OUT)

# =======================================================================
# because the connections between motors (right motor) and Raspberry Pi will be
# established, the being connected GPIO pins of Raspberry Pi
# such as MotorLeft_A, MotorLeft_B, and MotorLeft_PWM
# should be clearly declared whether their roles of pins
# are output pin or input pin
# =======================================================================
GPIO.setup(MotorRight_A,GPIO.OUT)
GPIO.setup(MotorRight_B,GPIO.OUT)
GPIO.setup(MotorRight_PWM,GPIO.OUT)

# =======================================================================
# create left pwm object to control the speed of left motor
# =======================================================================
LeftPwm=GPIO.PWM(MotorLeft_PWM,100)

# =======================================================================
# create right pwm object to control the speed of right motor
# =======================================================================
RightPwm=GPIO.PWM(MotorRight_PWM,100)


def rightSwingTurn(speed, running_time):
	leftmotor(forward0)
	GPIO.output(MotorLeft_PWM,GPIO.HIGH)

	GPIO.output(MotorRight_PWM,GPIO.LOW)
	LeftPwm.ChangeDutyCycle(speed)
	RightPwm.ChangeDutyCycle(0)
	sleep(running_time)

def leftSwingTurn(speed, running_time):
    rightmotor(forward0)
    GPIO.output(MotorRight_PWM,GPIO.HIGH)

    GPIO.output(MotorLeft_PWM,GPIO.LOW)
    RightPwm.ChangeDutyCycle(speed)
    LeftPwm.ChangeDutyCycle(0)
    sleep(running_time)

# student assignment (2) rightPointTurn() v

def rightPointTurn(speed, running_time):
    # set the left motor to go forward
    leftmotor(forward0)
    GPIO.output(MotorLeft_PWM,GPIO.HIGH)

    # set the right motor to go forward
    rightmotor(backward0)
    GPIO.output(MotorRight_PWM,GPIO.HIGH)

    # set the speed of the left motor to go forward
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to go forward
    RightPwm.ChangeDutyCycle(speed)
    # set the running time of the left motor to go forward
    sleep(running_time)

def leftPointTurn(speed, running_time):
    rightmotor(forward0)
    GPIO.output(MotorRight_PWM,GPIO.HIGH)

    leftmotor(backward0)
    GPIO.output(MotorLeft_PWM,GPIO.HIGH)

    RightPwm.ChangeDutyCycle(speed)
    LeftPwm.ChangeDutyCycle(speed)
    sleep(running_time)
