from time import time
from math import sqrt

start = time()

primes = [2,3]

def isPrime(n):
	if n < 2: 
		return False

	if n in primes:
		return True

	limit = int(sqrt(n)+1)
	for prime in primes:
		if prime > limit:
			primes.append(n)
			return True
		if n % prime == 0:
			return False

	for x in range(primes[-1]+1,limit):
		if n % x == 0:
			return False

	primes.append(n)
	return True

def getMostConsecutivePrimes(a,b):
	# a and b > 0
	primesPlusPlus = 0
	plusPlus = True

	# a > 0 and b < 0
	primesPlusMinus = 0
	plusMinus = True

	# a < 0 and b > 0
	primesMinusPlus = 0
	minusPlus = True

	# a and b < 0
	primesMinusMinus = 0
	minusMinus = True
	
	cont = True
	n = 0
	finished = []
	while cont:
		#both are positive
		if plusPlus:
			val = n**2 + n*a + b
			if isPrime(val):
				primesPlusPlus += 1
			else:
				plusPlus = False
				finished.append([a,b,primesPlusPlus])
		
		#a positive, b negative
		if plusMinus:
			val = n**2 + n*a - b
			if isPrime(val):
				primesPlusMinus += 1
			else:
				plusMinus = False
				finished.append([a,-b,primesPlusMinus])

		#a negative, b positive
		if minusPlus:
			val = n**2 - n*a + b
			if isPrime(val):
				primesMinusPlus += 1
			else:
				minusPlus = False
				finished.append([-a,b,primesMinusPlus])

		#both are negative
		if minusMinus:
			val = n**2 - n*a - b
			if isPrime(val):
				primesMinusMinus += 1
			else:
				minusMinus = False
				finished.append([-a,-b,primesMinusMinus])

		cont = (plusPlus or plusMinus or minusPlus or minusMinus)
		n += 1
	#print str(finished[-1][0]) + ' and ' +  str(finished[-1][1]) + ' get ' + str(finished[-1][2]) + ' consecutive primes'
	return finished[-1]

def main():
	aMax = 0
	bMax = 0
	conPrimes = 0
	try:
		for a in range(0,1000):
			for b in range(0,1000):
				(currentA,currentB,currenPrimes) = getMostConsecutivePrimes(a,b)
				if currenPrimes > conPrimes:
					aMax = currentA
					bMax = currentB
					conPrimes = currenPrimes
	except KeyboardInterrupt:
		print str(a) + ' and ' + str(b)
	print 'The value is ' + str(aMax*bMax) + ' with ' + str(conPrimes) + ' consecutive primes (execution took ' + str(time()-start) + ' seconds)'

main()
			
