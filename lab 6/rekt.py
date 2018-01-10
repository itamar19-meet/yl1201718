from turtle import *
import random
import time
colormode(255)
tracer(0)
ht()
class Circle(Turtle):
	def __init__(self,color,height,x,y,width):
		Turtle.__init__(self)
		self.pu()
		self.x = x
		self.y = y 
		self.goto(x,y)
		self.shape("circle")
		
		self.height = height
		self.width = width
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color(r,g,b)
	def move(self):
		current_x = self.xcor()
		current_y = self.ycor()
		self.goto(current_x + self.dx , current_y + self.dy)
	def collission(self,height,width,y,x):
		rect1_right = rect1.xcor()+(rect1.width()/2)
		rect1_left = rect1.xcor()-(rect1.width()/2)
		rect1_top = rect1.ycor()+(rect1.height()/2)
		rect1_bott = rect1.ycor()-(rect1.height()/2)
		rect2_right = rect2.xcor()+(rect2.width()/2)
		rect2_left = rect2.xcor()-(rect2.width()/2)
		rect2_top = rect2.ycor()+(rect2.height()/2)
		rect2_bott = rect2.ycor()-(rect2.height()/2)
		