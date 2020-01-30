#!/usr/bin/env python

def get_tuple_copy(lim):
	new = ()
	for i in range(lim):
		new = new + (i,)
	return new

def get_list_copy(lim):
	new = []
	for i in range(lim):
		new.append(i)
	return new

if __name__ == '__main__':
	import timeit
	lim = int(input("Set a range value: "))
	tuple_setup = "from __main__ import get_tuple_copy"
	list_setup = "from __main__ import get_list_copy"
	tuple_results = timeit.timeit("get_tuple_copy(lim)", setup=tuple_setup, globals=globals())
	list_results = timeit.timeit("get_list_copy(lim)", setup=list_setup, globals=globals())
	print(f"""
	Tuple: {tuple_results} seconds to complete 1000000 iterations
	List: {list_results} seconds to complete 1000000 iterations
	""")
