from turtle import *
import random
import math

class rekt(Turtle):
	def __init__(self,X1,X2,Y1,Y2):
		Turtle.__init__(self)
		self.width = math.fabs(X1 - X2)
		self.height = math.fabs(Y1-Y2)

		self.X1 = X1
		self.X2 = X2
		self.Y1 = Y1
		self.Y2 = Y2
	def getrekt(self):
		for i in range(2):
			self.forward(self.width)
			self.left(90)
			self.forward(self.height)
			self.left(90)
	def coco(self,rect_1,rect_2):
		if (rect_1.Y2 >= rect_2.Y1 and rect_1.X2 >= rect_2.X1 and rect_1.Y1 <= rect_2.Y2 and rect_1.X1 <= rect_2.X2):
			print("oh my gahhhh")

			
rect_1 = rekt(10,10,10,10)

rect_2 = rekt(-100,-100,-100,-100)
rect_1.getrekt()
rect_2.getrekt()

rect_1.coco(rect_1,rect_2)






mainloop()