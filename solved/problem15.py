import sys
import time

def factorial(n):
    if n == 1:
	return 1
    else:
	return n * factorial(n - 1)

def number_of_routes(dimX,dimY):
    #Binomial coefficient: (n + m)! / m! * n!
    start = time.clock()
    n = factorial(dimX + dimY) / (factorial(dimY) * factorial(dimX))
    print 'Number of routes for ' + str(dimX) + 'X' + str(dimY) + ' grid: ' + str(n) + '(calculated in ' + str(time.clock() - start) + ')'

def main():
    start = time.clock()
    for i in xrange(1,21):
	number_of_routes(i,i)
    print 'Total time: ' + str(time.clock() - start)

main()
