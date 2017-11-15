class person(object):
	def __init__(self,name,age,f_food,city):
		self.name = name
		self.age = age
		self.f_food = f_food
		self.city = city
	def man(self,name,age,f_food,city):
		print(" his name is " + name + " and he is "+ age + " and he like to eat" + f_food + " and he lives in "+city)
	def breakfst(self , f_food):
		print("he likes to eat"+f_food+" for breakfast")
a = person("itamar",15,"pizza","jerusalem")
a.breakfst("pizza")

