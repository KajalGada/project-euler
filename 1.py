#!/usr/bin/env python3

#Project Euler
#Problem 1: Multiples of 3 and 5

sum = 0

for i in range(1,1000):
	# print (i)
	if i%3 == 0:
		sum = sum + i
	elif i%5 == 0:
		sum = sum + i

print ('Sum:',sum)

