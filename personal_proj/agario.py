from turtle import*
from Ball import my_Ball
from random import*
import time

hideturtle()
tracer(0)
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH=int(getcanvas().winfo_width()/2)
SCREEN_HEIGHT=int(getcanvas().winfo_height()/2)

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
	NEW_BALL= my_Ball(x, y, dx, dy, rad)
	BALLS.append(NEW_BALL)
def collide(ball_b,ball_a):
	if(ball_a.rad + ball_b.rad)>sqrt( (ball_a.x - ball_b.x)**2 + ((ball_a.y - ball_b.y)**2 )):
		if(ball_a.rad < ball_b.rad):
			return True
		elif(ball_a.rad> ball_b.rad):
			return False
def check_all_balls_collision():
	for p in BALLS:
		for g in BALLS:
			if(collide(i,g)):

	
			
def check_myball_collision():
	for m in BALLS:
		if(collide(m,my_Ball)):

			
def move_around(event):
	my_Ball.goto(event.x -SCREEN_WIDTH,SCREEN_HEIGHT - event.y)

getcanvas().bind("<Motion>", move_around)
listen()
while RUNNING == True:
	check_myball_collision()
	check_all_balls_collision()











mainloop()








