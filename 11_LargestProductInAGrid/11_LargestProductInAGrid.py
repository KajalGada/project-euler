# ------------------------------------------------------
# 	Project Euler
# 	Problem 11_LargestProductInAGrid.py
# 	Kajal Damji Gada | Created: 5th March 2017
# ------------------------------------------------------

import time
startTime = time.time()	#Timer

#Read content from file and arrange in a 2D array.
fileHandle = open('11_LargestProductInTheGrid_Numbers.txt','r')

grid = []
for line in fileHandle:
	lineStr = line[:-1] 					#To remove new line character
	lineStrSplit = lineStr.split(' ')
	row = []
	for num in lineStrSplit:
		row.append(int(num))
	grid.append(row)

#Loop through each element and look at product along 4 directions
n = 4  										#Number of adjacent numbers
productMax = 1
productDig2 = 1
for r in range(len(grid)):
	for c in range(len(grid[0])):

		if (c+n-1) < len(grid[0]):
			productRow = grid[r][c]
			for k in range(1,n):
				productRow = productRow * grid[r][c+k]

		if (r+n-1) < len(grid):
			productCol = grid[r][c]
			for k in range(1,n):
				productCol = productCol * grid[r+k][c]

			if (c+n-1) < len(grid[0]):
				productDig = grid[r][c]
				for k in range(1,n):
					productDig = productDig * grid[r+k][c+k]

			if (c-n-1) > -1:
				productDig2 = grid[r][c]
				for k in range(1,n):
					productDig2 = productDig2 * grid[r+k][c-k]

		productMax = max(productRow,productCol,productDig,productDig2,productMax)

print "Max of " , n , " adjacent numbers is: " , productMax

runTime = time.time() - startTime
print "Time to run: " , runTime