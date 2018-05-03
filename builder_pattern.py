#!/usr/bin/python3

from enum import Enum
import time

# An example of a simple builder function.
# Let's take baking pizza for example.

PizzaProgress = Enum("PizzaProgress", "queued, prepartion, baking, ready")
PizzDough = Enum("PizzDough", "thin, thick")
PizzaSauce = Enum("PizzaSauce", "tomato, creme_fraiche")
PizzaTopping = Enum("PizzaTopping", "mozzarella, bacon")
STEP_DELAY = 3 # second time


class Pizza:
	def __init__(self, name):
		self.name = name
		self.dough = None
		self.sauce = None
		self.topping = []
		self.progress = None

	def __str__(self):
		return self.name

	def prepare_dough(self, dough):
		self.dough = dough
		print("prepare the %s dough of your %s." % (self.dough.name, self))
		time.sleep(STEP_DELAY)
		print("done with the %s dough" % self.dough.name)


class FirstPizza:
	def __init__(self):
		self.pizza = Pizza("first")
		self.progress = PizzaProgress.queued
		self.baking_time = 5

	def prepare_dough(self):
		self.progress = PizzaProgress.prepartion
		self.pizza.prepare_dough(PizzDough.thin)

	def add_sauce(self):
		print("adding the tomato sauce to your first pizza")
		self.pizza.sauce = PizzaSauce.tomato
		time.sleep(STEP_DELAY)
		print("done with the tomato sauce")

	def add_topping(self):
		print("adding the topping(%s) to your first pizza" % PizzaTopping.mozzarella)
		self.pizza.topping.append(PizzaTopping.mozzarella)
		time.sleep(STEP_DELAY)
		print("done with the topping(mozzarella)")

	def bake(self):
		self.progress = PizzaProgress.baking
		print("baking your first pizza for %s seconds" % self.baking_time)
		time.sleep(self.baking_time)
		self.progress = PizzaProgress.ready
		print("your first pizza is ready")


class Waiter:
	def __init__(self):
		self.build_pizza = None

	def pizza_build(self, builder):
		self.build_pizza = builder
		self.build_pizza.prepare_dough()
		self.build_pizza.add_sauce()
		self.build_pizza.add_topping()
		self.build_pizza.bake()

	@property
	def get_pizza(self):
		return self.build_pizza.pizza


def main():
	waiter = Waiter()
	waiter.pizza_build(FirstPizza())
	pizza = waiter.get_pizza
	print("Enjoy your %s pizza!" % pizza)


if __name__ == "__main__":
	main()
