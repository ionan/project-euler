from math import sqrt
import time

start_time = time.time()

def sumOfDivisors(n):
	s = 1
	candidate = 2
	limit = int(sqrt(n) + 1)
	while candidate < limit:
		if n % candidate == 0:
			rest = (n / candidate)
			s += candidate
			if rest != candidate:
				s += rest
		candidate += 1
	#print str(n) + ' = ' + str(s)
	return s

def main():
	abundantNumbers = set()
	sumOfIntegers = 0
	for x in range(1,28124):
		s = sumOfDivisors(x)
		if s > x:
			abundantNumbers.add(x)
		sumOfIntegers += x

	abundantSums = set()
	for i in abundantNumbers:
		for j in abundantNumbers:
			cnd = i + j
			if cnd < 28124:
				abundantSums.add(cnd)

	sumOfIntegers -= sum(abundantSums)

	print 'Sum is ' + str(sumOfIntegers) + ' (execution took ' + str(time.time() - start_time) + ' seconds)'


main()
