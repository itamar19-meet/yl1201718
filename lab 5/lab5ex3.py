from turtle import *

print("succ my ducc . 2 + 2 is 4 minus 1 thats 3 quick math everyday mans on the bloock moke trees se your girl in the park that girl is a uckers when the ting went quack quack quack you men were ducking hold tight asznee he is got a pumpy hold tight my man he is got a frizby i trap trap trap on the road moving that cornflakes rice crispies hold tight my girl witnee on the road doing ten toes like my toes you men thought i froze i see a peng girl then i pose  if she aint on it im ghost look at your nose what you dickhead! look at your nose nose looking like a garden hose ay you get me gah. hop out of the four door with a 44 it was 1 2 3 and 4 chilling in the corridor your dad is 44 and he is still calling man for a draw let him know when i see him im gonna spin he's jaw take mans twix by force send mans shop by force your girl knows ive got the sauce no ketchop just sauce raw sauce ah ye boom gah the ting goes skrrrrah pah pah pah ka ka skibidi ka ka and a purru purru pum pum pum skya pum pum pum pum pum pum . poom poom you don know")
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
		self.speed(speed)
	
		self.color(color)

big_shaq = Hexagon(2,10,"blue")

for i in range(360):
	big_shaq.forward(2)
	big_shaq.right(1)
for x in range(20):
	big_shaq.pu()
	big_shaq.right(100)
	big_shaq.pd()
	for i in range(360):
		big_shaq.forward(2)
		big_shaq.right(1)

	
big_shaq.hideturtle()
mainloop()