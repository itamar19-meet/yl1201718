

class Animal(object):
	def __init__(self,name,age,fav_color,favfood,make_sound):
		self.name = name
		self.age = age
		self.fav_color = fav_color
		self.favfood = favfood
		self.make_sound = make_sound


	def eat(self,favfood):
		print("ayy " + self.name + " loves " + favfood)
	def descrip(self):
		print(self.name + "is" + self.age+"years old and loves color" + self.fave_color)
	def sound(self , makesound):
		x = input("how man time do u want the cat to say meow?")
		print("cat is saying " +( self.make_sound * x))
a = Animal("cat",12,"red","lasagna","meow")
a.eat ("lasagna")
a.sound("meow")



