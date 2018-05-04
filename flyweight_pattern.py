#!/usr/bin/python3

import random
from enum import Enum


Type_Tree = Enum("Type_Tree", "apple_tree, cherry_tree, peach_tree")


class Tree:
	pool = dict()

	def __new__(cls, type_tree):
		obj = cls.pool.get(type_tree)
		if not obj:
			obj = object.__new__(cls)
			cls.pool[type_tree] = obj
			obj.type_tree = type_tree
		return obj

	def render(self, age, point_min, point_max):
		print("render the {} tree and age is {} at ({}, {})".format(self.type_tree, age, point_min, point_max))


def main():
	rnd = random.Random()
	age_min, age_max = 1, 30
	point_min, point_max = 1, 100
	tree_countes = 0

	for _ in range(10):
		tree = Tree(Type_Tree.apple_tree)
		tree.render(rnd.randint(age_min, age_max),
			rnd.randint(point_min, point_max),
			rnd.randint(point_min, point_max))
		tree_countes += 1

	for _ in range(3):
		tree = Tree(Type_Tree.cherry_tree)
		tree.render(rnd.randint(age_min, age_max),
			rnd.randint(point_min, point_max),
			rnd.randint(point_min, point_max))
		tree_countes += 1

	for _ in range(3):
		tree = Tree(Type_Tree.peach_tree)
		tree.render(rnd.randint(age_min, age_max),
			rnd.randint(point_min, point_max),
			rnd.randint(point_min, point_max),)
		tree_countes += 1

	print("All tree: {}, type: {}".format(tree_countes, len(Tree.pool)))


if __name__ == "__main__":
	main()
