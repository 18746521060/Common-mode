#!/usr/bin/python3

# Factory model example

class Botany:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

	def execute(self, obstacle):
		print("the {} Botany encounters {} and {}".format(self, obstacle, obstacle.action()))

class Corpse:
	def __str__(self):
		return "a hungry zombie"

	def action(self):
		return "kills it"


class BotanyWorld:
	"""
	Associate Botany and Corpse.
	"""
	def __init__(self, name):
		print(self)
		self.player_name = name

	def __str__(self):
		return "\n\t------ Botany World ------"

	def make_charactor(self):
		return Botany(self.player_name)

	def make_obstacle(self):
		return Corpse()


class Police:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

	def execute(self, obstacle):
		print("a {} Police encounters {} and {}".format(self, obstacle, obstacle.action()))


class Scoundrel:
	def __str__(self):
		return "a evil Scoundrel"

	def action(self):
		return "catches it"


class PoliceWorld:
	"""
	Associate Police and Scoundrel.
	"""
	def __init__(self, name):
		print(self)
		self.player_name = name

	def __str__(self):
		return "\n\t------ Police World ------"

	def make_charactor(self):
		return Police(self.player_name)

	def make_obstacle(slef):
		return Scoundrel()


class GameEvenment:
	def __init__(self, factory):
		self.hero = factory.make_charactor()
		self.obstacle = factory.make_obstacle()

	def play(self):
		self.hero.execute(self.obstacle)


def validate_age(name):
	age = input("Welcome {}. How old are you?".format(name))
	try:
		age = int(age)
	except ValueError as e:
		print("This age format is not correct:{}".format(age))
		return (False, age)
	if age <= 0:
		print("Age must be a positive integer.")
		return (False, age)
	return (True, age)

def main():
	name = input("Hello. What's your name?")
	age_status = False
	while not age_status:
		age_status, age = validate_age(name)
	game = BotanyWorld if age < 18 else PoliceWorld
	GameEvenment(game(name)).play()

if __name__ == "__main__":
	main()