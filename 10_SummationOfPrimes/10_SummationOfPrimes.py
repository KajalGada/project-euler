#Generating List of Prime Numbers

import time
startTime = time.time()	#Timer

n = 2000000
primeNumSet = set()
compNumSet = set()

primeNumSet.add(2)
total = 2
for num in xrange(3,n+1,2):
	if num not in compNumSet:
		primeNumSet.add(num)
		total = total + num
		for u in xrange(num*num,n,num*2):
			compNumSet.add(u)

print "Total of prime numbers below ",n," is: ",total

runTime = time.time() - startTime
print runTime