import turtle
turtle.pencolor("Yellow")
colors = ["Red","Blue","Green","Purple","Black"]
turtle.pensize(10)
for i in range(5):
	turtle.forward(100)
	turtle.left(144)
	turtle.pencolor(colors[i])
turtle.mainloop()