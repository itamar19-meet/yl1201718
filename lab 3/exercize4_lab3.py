import turtle
turtle.speed(50)
a = 0

turtle.pendown()
for i in range(180):
	turtle.forward(100)
	turtle.right(45)
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(25)
	turtle.penup()
	turtle.setposition(0, 0)

	
	turtle.pendown()
	turtle.home()
	
	turtle.right(a)
	a+=2
	
turtle.mainloop()