from turtle import*
from Ball import my_Ball
import random 
import time
import math
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
	x = random.randint((-SCREEN_WIDTH) + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
	y = random.randint((-SCREEN_HEIGHT)+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	rad = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color = color
	NEW_BALL= my_Ball(x, y, dx, dy, rad)
	BALLS.append(NEW_BALL)
def move_all_balls():
	for lol in BALLS:
		move_width = random.randint((-SCREEN_WIDTH) + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
		move_height = random.randint((-SCREEN_HEIGHT)+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
		lol.goto(move_width,move_height)
def collide(ball_a,ball_b):
	temp_a_x = ball_a.xcor()
	temp_a_y = ball_a.ycor()
	temp_b_x = ball_b.xcor()
	temp_b_y = ball_b.ycor()
	distance = math.sqrt(math.pow(temp_b_x - temp_a_x, 2)+math.pow(temp_b_y - temp_a_y, 2))+10
	rads = ball_a.rad+ball_b.rad
	if(rads>distance):
		return True
	if(rads<distance):
		return False
def check_all_balls_collision():
	for ball_b in BALLS:
		for ball_a in BALLS:
			if(collide(ball_a,ball_b)):
				ball_ar = ball_a.rad
				ball_br = ball_b.rad
				rand_x_cor = random.randint(-SCREEN_WIDTH, SCREEN_WIDTH)
				rand_y_cor = random.randint(-SCREEN_HEIGHT, SCREEN_HEIGHT)
				rand_dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				rand_dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				rand_rad = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				rand_r = random.randint(0, 255)
				rand_g = random.randint(0, 255)
				rand_b = random.randint(0, 255)
				rand_color = (rand_r, rand_g, rand_b)

				if(ball_br < ball_ar):
					print("ball a is bigger")
					ball_b.goto(rand_x_cor,rand_y_cor)
					ball_b.dx = rand_dx
					ball_b.dy = rand_dy
					ball_b.rad = rand_rad
					ball_b.color = (rand_r, rand_g, rand_b)
					ball_a.rad+=1
					ball_b.shapesize(ball_b.rad/10)
					ball_a.shapesize(ball_a.rad/10)
				if ball_ar == ball_br:
					pass
				if(ball_ar<ball_br):
					print("ball b is bigger")
					ball_a.goto(rand_x_cor,rand_y_cor)
					ball_a.dx = rand_dx
					ball_a.dy = rand_dy
					ball_a.rad = rand_rad
					ball_a.color = (rand_r, rand_g, rand_b)
					ball_b.rad+=1
					ball_b.shapesize(ball_b.rad/10)
					ball_a.shapesize(ball_a.rad/10)
def check_myball_collision():
	for m in BALLS:
		if(collide(m,MY_BALL)):
			rand_x_cor = random.randint(-SCREEN_WIDTH, SCREEN_WIDTH)
			rand_y_cor = random.randint(-SCREEN_HEIGHT, SCREEN_HEIGHT)
			rand_dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
			rand_dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
			rand_radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
			rand_r = random.randint(0, 255)
			rand_g = random.randint(0, 255)
			rand_b = random.randint(0, 255)
			rand_color = (rand_r, rand_g, rand_b)
				
			if(MY_BALL.rad<m.rad):
				return False
			if(MY_BALL.rad>m.rad):
				print("my ball is bigger")
				m.goto(rand_x_cor,rand_y_cor)
				m.dx = rand_dx
				m.dy = rand_dy
				m.rad = rand_rad
				m.color = (rand_r, rand_g, rand_b)
				MY_BALL.rad+=1
				m.shapesize(m.rad/10)
				MY_BALL.shapesize(MY_BALL.rad/10)
				return True
def move_around(event):
	MY_BALL.goto(int(event.x -SCREEN_WIDTH),int(SCREEN_HEIGHT - event.y))

getcanvas().bind("<Motion>", move_around)
listen()
while RUNNING == True:
	move_all_balls()
	check_myball_collision()
	check_all_balls_collision()
	getscreen().update()

	time.sleep(SLEEP)











mainloop()








