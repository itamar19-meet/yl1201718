from turtle import *
import random
import math

class circle(Turtle):
	def __init__(self,radius ,color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.color(color)
		self.radius = radius
		self.speed(speed)
circle1 = circle(100,"red",10)
circle2 = circle(80,"blue",10)
circles = []
circles.append(circle1)
circles.append(circle2)



def checc_ccolision(circle1,circle2):
	y1 = circle1.xcor()
	x1 = circle1.xcor()
	y2 = circle2.ycor()
	x2 = circle2.ycor()
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if D <= circle1.radius + circle2.radius:
		print("oh no. collision")
	else:
		print("the circles are fine")

checc_ccolision(circle1, circle2)
mainloop()