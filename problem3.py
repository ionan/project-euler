import sys
import time
import math
from math import sqrt

numbers = []
primes = []
number = 600851475143

def main():
    start = time.clock()
    #Sieve of Erathostenes
    #create a list with numbers from 1 to sqrt(number)
    for i in xrange(3,int(sqrt(number)),2):
	if 600851475143 % i == 0:
	    numbers.append(i)

    for j in xrange(len(numbers)):
	if numbers[j] != 0:
	    primes.append(numbers[j])
	    for k in xrange(j+1,len(numbers)):
		if numbers[k] != 0 and numbers[k] % numbers[j] == 0:
		    numbers[k] = 0 

    print 'Largest prime factor of 600851475143: ' + str(primes[-1]) + '(calculated in ' + str(time.clock() - start) + ')'
    print 'List of primes: ' + str(primes)

main()
