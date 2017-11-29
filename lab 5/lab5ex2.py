from turtle import *
import random
colormode(255)
class Square(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shapesize(size)
		
		self.shape("square")

	def random_color(self):
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color(r,g,b)
square1 = Square(15)
square1.random_color()

###hexa >||||


begin_poly()
for i in range(6):
	forward(50)
	left(60)
end_poly()
shape1 = get_poly()
register_shape("hexagon",get_poly())
class Hexagon(Turtle):
	def __init__(self,size ,speed,color):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape("hexagon")
		self.speed(seed)
	
		hexagon.color("red")

big_shaq = Hexagon(2,10,"blue")

mainloop()

