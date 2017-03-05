#Project Euler: Problem 11 Largest Product in a grid

##Problem Statement
What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
Grid stored in text file

##Approach
+Loop through all numbers and look at product along each direction.
+Only need to look at 4 directions and not 8 as the other 4 are considered by another number.
+Care needs to be taken when dealing with boundary numbers.
