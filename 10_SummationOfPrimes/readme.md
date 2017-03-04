#Project Euler

##Problem 10: Summation of Primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

##Solution
For optimization:
+ *Sieve of Eratosthenes:* knock of multiples of prime numbers. That is, once 3 is identified as prime number no need to check multiples of 3: 6,9,12,15, etc. Thus, maintain a set of prime numbers and its multiples (composite numbers). 
+ *Set:* Use set instead of list as lookup for list is time-consuming.
+ *Odd numbers:* Only look at odd numbers to speed up the process.

##Pseudo-code:
```
for each num:
  if not composite:
    add to prime num list
    add its multiples in composite num list
```
