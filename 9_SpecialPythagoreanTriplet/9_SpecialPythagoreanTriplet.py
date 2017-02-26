# ------------------------------------------------------
# 	9_SpecialPythagoreanTriplet.py
# 	Kajal Damji Gada | Created: 25th Feb 2017
# ------------------------------------------------------

from math import sqrt

Total = 1000

print "Problem 9: Special Pythagorean Triplet"

b = 1
outerLoop = 0

while outerLoop == 0:
	b = b + 1
	a = 1
	innerLoop = 0
	while innerLoop == 0:
		c = sqrt(a**2 + b**2)
		if a + b + c == Total:
			innerLoop = 1
			outerLoop = 1
		elif a == (b-1):
			innerLoop = 1
		else:
			a = a + 1

print "a = " ,a ," b = " ,b ," c = " ,c 
print "a*b*c = " ,a*b*c 