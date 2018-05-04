#!/usr/bin/python3

#

from functools import wraps


def num_decorator(fn):
	known = dict()

	wraps(fn)
	def get_known(*args):
		if args not in known:
			known[args] = fn(*args)
		return known[args]

	return get_known


@num_decorator
def n_sum(n):
	"""
	获取0-n中所有整数的和
	"""
	assert n >= 0, "n必须大于等于零"
	return n if n == 0 else n + n_sum(n-1)


def no_decorator_n_sum(n):
	assert n >= 0, "n必须大于等于零"
	return n if n == 0 else n + n_sum(n-1)	


@num_decorator
def fibonacci(n):
	"""
	获取第n个斐波那契的数
	"""
	assert n >= 0, "n必须大于等于零"
	return n if n in (0, 1) else fibonacci(n - 1) + fibonacci(n - 2)


def no_decorator_fibonacci(n):
	assert n >= 0, "n必须大于等于零"
	return n if n in (0, 1) else fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
	from timeit import Timer

	t = Timer("n_sum(300)", "from __main__ import n_sum").timeit()
	t2 = Timer("no_decorator_n_sum(300)", "from __main__ import no_decorator_n_sum").timeit()
	print("s_sum: %s\nno_decorator_n_sum: %s" % (t, t2))

	t3 = Timer("fibonacci(200)", "from __main__ import fibonacci").timeit()
	t4 = Timer("no_decorator_fibonacci(200)", "from __main__ import no_decorator_fibonacci").timeit()
	print("fibonacci: %s\nno_decorator_fibonacci: %s" % (t3, t4))

	print(n_sum(300) == no_decorator_n_sum(300))
	print(fibonacci(200) == no_decorator_fibonacci(200))
