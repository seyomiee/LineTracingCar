import RPi.GPIO as GPIO
GPIO.setwarnings(False)

from time import sleep
from ultraModule import getDistance
from go_any import *
from TurnModule import *

###########################################
from trackingModule import getTracking

#####################INITIALIZATION VALUES
dis = 20
SwingPr = 40
SwingTr = 1.2
SwingPl = 60
SwingTl = 1.5
#PointPr = 20
#PointTr = 0.6
###########################################

def linetracing():
	tracking = getTracking()
	result = 0
	for i in range(0, 5):
		result = result + (tracking[i] << i)

	distance = getDistance()
	print('distance= ', distance)

	if(dis > distance):
		stop()
		sleep(1)
		rightSwingTurn(SwingPr,SwingTr)
		stop()
		sleep(1)
		go_forward(60,1.2)
		leftSwingTurn(SwingPl,SwingTl)

		go_forward(20,1)
# =======================================================================
# the algorithm of line tracing
# ---------------------------------------------------------------------
# forward case when line tracing : [DBACE]=[1xxx1]
# ---------------------------------------------------------------------
# 1) [11011] : meets forward narrow line when line tracing
# --> fornaw
# 2) [10001] : meets forward wide line when line tracing
# --> forwide
	if(result == 0b11011):
		go_forward_any(30,30)
	if(result == 0b10001):
		go_forward_any(30,30)
# ---------------------------------------------------------------------
# left turn case when line tracing : [DBACE]=[xxx11]
# ---------------------------------------------------------------------
# 1) [01111] : meets left-turn 1st narrow line when line tracing
# --> ltnarfirst
# 2) [00111] : meets left-turn 1st wide line when line tracing
# --> ltwidfirst
# 3) [00011] : meets left-turn wider line when line tracing
# --> ltwider
# 4) [10111] : meets left-turn 2nd narrow line when line tracing
# --> ltnarsecond
# 5) [10011] : meets left-turn 2nd wide line when line tracing
# --> ltnarsecond
	if(result == 0b01111):
		go_forward_any(0,30)
	if(result == 0b00111):
		go_forward_any(30,30)
	if(result == 0b00011):
		go_forward_any(30,0)
	if(result == 0b10111):
		go_forward_any(30,30)
	if(result == 0b10011):
		go_forward_any(20,30)
# ---------------------------------------------------------------------
# right turn case when line tracing : [DBACE]=[11xxx]
# ---------------------------------------------------------------------
# 1) [11110] : meets right-turn 1st narrow line when line tracing
# --> rtnarfirst
# 2) [11100] : meets right-turn 1st wide line when line tracing
# --> rtwidfirst
# 3) [11000] : meets right-turn wider line when line tracing
# --> rtwider
# 4) [11101] : meets right-turn 2nd narrow line when line tracing
# --> rtnarsecond
# 5) [11001] : meets right-turn 2nd wide line when line tracing
# --> rtnarsecond
	if(result == 0b11110):
		go_forward_any(30,10)
	if(result == 0b11100):
		go_forward_any(30,15)
	if(result == 0b11000):
		go_forward_any(30,15)
	if(result == 0b11101):
		go_forward_any(30,20)
	if(result == 0b11001):
		go_forward_any(30,20)


def setup():
	LeftPwm.start(0)
	RightPwm.start(0)

if __name__ == '__main__':
	try:
		setup()
#		motor()
		while True:
			linetracing()
	except KeyboardInterrupt:
		stop()
		GPIO.cleanup()
