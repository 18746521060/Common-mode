#!/usr/bin/python3


class Computer:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

	def run(self):
		print("the %s computer runs program" % self)


class Tv:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

	def show(self):
		print("the %s TV is showing the movie." % self)


class Adapter:
	def __init__(self, obj, method):
		self.obj = obj
		self.__dict__.update(dict(execute=method))


def main():
	computer = Computer("Lenovo")
	tv = Tv("Konka")
	example = [Adapter(computer, computer.run), Adapter(tv, tv.show)]
	for i in example:
		i.execute()


if __name__ == "__main__":
	main()
