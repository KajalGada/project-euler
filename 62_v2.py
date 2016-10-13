#!/usr/bin/env python

#Project Euler
#Problem 62: Cubic Permutations

import time
start_time = time.time()	#Timer

num = 100
no_cubes_req = 5
num_checked_list = {} #dict
stopWhile = True

while stopWhile is True:
	
	cube_value = num * num * num
	sorted_cube_digits = ''.join(sorted(str(cube_value)))

	if sorted_cube_digits in num_checked_list:
		num_checked_list[sorted_cube_digits] += [num]
		if len(num_checked_list[sorted_cube_digits]) is no_cubes_req:
			print num_checked_list[sorted_cube_digits]
			ans = num_checked_list[sorted_cube_digits][0]
			print ans*ans*ans
			time_run = time.time() - start_time
			print  'Time to run (in sec): ' ,time_run
			stopWhile = False
	else:
		num_checked_list[sorted_cube_digits] = [num]

	num += 1