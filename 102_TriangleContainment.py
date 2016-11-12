#!/usr/bin/env python

#Project Euler
#Problem 102: Triangle containment

from math import acos, sqrt, degrees
import time

start_time = time.time()

file_handle = open('p102_triangles.txt', 'r')
tot = 0

for i in range(1000):
	set_points = file_handle.readline()
	set_points_ = set_points[:-1]
	set_points_split = set_points_.split(',')

	a = [0,0,0,0]
	ang_sum = 0

	for j in (0,2,4):

		for k in range(4):
			ref = j + k
			if ref > 5:
				ref = ref - 6
			a[k] = int(set_points_split[ref])

		num = (a[0]*a[2]) + (a[1]*a[3])
		den_1 = sqrt((a[0]**2)+(a[1]**2))
		den_2 = sqrt((a[2]**2)+(a[3]**2))
		den = den_1 * den_2

		ang = acos(num/den)
		ang_sum = ang_sum + ang

	if degrees(ang_sum) > 359.99:
		tot = tot + 1

print tot
file_handle.close()

time_run = time.time() - start_time
print  'Time to run (in sec): ' ,time_run