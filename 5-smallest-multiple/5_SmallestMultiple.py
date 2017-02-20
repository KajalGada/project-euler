print "Project Euler > Problem 5: Smallest Multiple"

# ---------------------------------------------------------------
# 							TO DO
# ---------------------------------------------------------------
# Prime Number generate base list based on num starting with

# ---------------------------------------------------------------
# 							FUNCTIONS
# ---------------------------------------------------------------

def get_div(numCheck, primeNumbers):

	ind = 0
	divFlag = 0
	while divFlag == 0:
		div = primeNumbers[ind]
		if numCheck%div == 0:
			divFlag = 1
		else:
			ind = ind + 1

	return div


def get_prime_num(numCheck, primeNumbers):

	returnList = []
	primeNumFlag = 0
	div = get_div(numCheck, primeNumbers)

	while primeNumFlag == 0:
		if numCheck%div == 0:
			returnList.append(div)
			numCheck = numCheck/div
			if numCheck == 1:
				primeNumFlag = 1
		elif numCheck in primeNumbers:
			returnList.append(numCheck)
			primeNumFlag = 1
		else:
			div = get_div(numCheck, primeNumbers)

	return returnList

# ----------------------------------------------------
# 						MAIN
# ----------------------------------------------------

num = 20;
primeNumbers = [2,3,5,7,11,13,17,19]

primeNumList = []
for i in range(2,num+1):
	tempList = get_prime_num(i,primeNumbers)
	primeNumList.append(tempList)

# print primeNumList
lcmList = []

for eachList in primeNumList:

	for eachNum in eachList:
		lcmList.append(eachNum)

		for eachList_2 in primeNumList:

			if eachList_2.count(eachNum) > 0:
				eachList_2.remove(eachNum)

# print lcmList
lcmAns = 1

for eachMultiple in lcmList:
	lcmAns = lcmAns * eachMultiple

print lcmAns