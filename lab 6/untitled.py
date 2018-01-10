from turtle import *
import random
import time
colormode(255)
tracer(0)
ht()
class Circle(Turtle):
	def __init__(self,color,radius,x,y,dx,dy):
		Turtle.__init__(self)
		
		self.pu()
 		self.goto(x,y)
 		self.dx = dx
 		self.dy = dy
 		self.shape("circle")
 		self.shapesize(radius/10)
 		self.radius = radius
 		r = random.randint(0,255)
 		g = random.randint(0,255)
 		b = random.randint(0,255)
 		self.color(r,g,b)

 	def move(self):
 		current_x = self.xcor()
 		current_y = self.ycor()
 		self.goto(current_x + self.dx , current_y + self.dy)
circle1 = Circle(radius = 200,x = 0,y = 0,dx = 0.2,dy = 0.8)
circle2 = Circle(radius = 100,x = 20,y = -100 , dx = 0.7,dy = 0.10)
while True:
	circle1.move()
	circle2.move()
	getscreen().upload()
	time.sleep(.0077)

mainloop()