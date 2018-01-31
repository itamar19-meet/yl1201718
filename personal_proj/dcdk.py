from turtle import*
from random import*

colormode(255)
tracer(0)
ht()

class my_Ball(Turtle):   
	def __init__(self,x,y,dx,dy,rad):
		Turtle.__init__(self)
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.rad = rad
		self.shape("circle")
		r = randint(0,255)
		g = randint(0,255)
		b = randint(0,255)
		self.color(r,g,b)
		

	def move(self,SCREEN_HEIGHT,SCREEN_WIDTH):
		current_x = self.xcor()
		current_y = self.ycor()
		new_x = current_x+self.dx
		new_y = current_y+self.dy
		right_side_ball = new_x + self.rad
		left_side_ball = new_x - self.rad
		top_ball = new_y + self.rad
		bottom_ball = new_y - self.rad
		self.goto(new_x,new_y)
		if(right_side_ball >= SCREEN_WIDTH):
			self.dx = -self.dx

		if(left_side_ball <=(-SCREEN_WIDTH)):
			self.dx = -self.dx

		
		if(top_ball>=SCREEN_HEIGHT):
			self.dy = -self.dy

		if(bottom_ball<=(-SCREEN_HEIGHT)):
			self.dy = -self.dy



def collide(ball_a,ball_b):
	if(ball_a.rad+ball_b.rad)>sqrt( (ball_a.x - ball_b.x)**2 + sqrt((ball_a.y - ball_b.y)**2 )):
		return True
	else:
		return False
mainloop()