from turtle import*
from Ball import my_Ball
from random import*
import time

hideturtle()
tracer(0)
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH=getcanvas().winfo_width()/2
SCREEN_HEIGHT=getcanvas().winfo_height()/2
MY_BALL = my_Ball(0,0,1,1,10)
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS= 10
MAXIMUM_BALL_RADIUS= 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5
BALLS = []

for i in range(NUMBER_OF_BALLS):
	x = randint((-SCREEN_WIDTH) + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
	y = randint((-SCREEN_HEIGHT)+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
	dx = randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy = randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	rad = randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color = color
	NEW_BALL= BALLS(x, y, dx, dy, rad)
	BALLS.append()

for i in BALLS:
	NEW_BALL.move(SCREEN_HEIGHT,SCREEN_WIDTH)

def collide():
	
