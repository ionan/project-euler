from time import time

start = time()

def matches(n):
	s = str(n)
	sumOfPowers = 0
	for char in s:
		sumOfPowers += int(char)**5
		if sumOfPowers > n:
			return False
	return (sumOfPowers == n)

def main():
	#Max number with 7 digits is 9999999
	#Sum of fifth powers is 413343 (just six digits)
	#That will be the limit
	limit = 1000000
	sumOfNumbers = 0
	for x in range(2,limit):
		if matches(x):
			sumOfNumbers += x
			print '\tNumber found: ' + str(x)

	print 'The sum of all numbers is ' + str(sumOfNumbers) + ' (execution took ' + str(time()-start) + ' seconds)'

main()
