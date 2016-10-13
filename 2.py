#!/usr/bin/env python3

#Project Euler
#Problem 2: Even Fibonacci numbers

a = 1
b = 1

sum = 0

while b < 4000000:

	next_num = a + b
	a = b
	b = next_num

	# print ('a,b:', a,b)

	if b%2 == 0:
		sum = sum + b

print ('Sum:',sum)

