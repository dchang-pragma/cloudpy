import class_rabbit

class DerivedRabbit(class_rabbit.Rabbit):
	def favorite_food(self,food):
		self.foods.append(food)

bunny5 = DerivedRabbit('Super Rabbit','Giant Rabbit','brown')