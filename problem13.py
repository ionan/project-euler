import sys
import time
import gmpy2
from gmpy2 import mpz

numbers = [] 

def read_numbers():
    f = open('./numbers.dat', 'r')
    for line in f:
	numbers.append(mpz(line))

def main():
    start = time.clock()
    read_numbers()
    number_sum = 0
    for item in numbers:
	number_sum = mpz(number_sum + item)

    #except KeyboardInterrupt:
    #    print 'Current sum: ' + str(number_sum) + '(calculated in ' + str(time.clock() - start) + ')'
    #    sys.exit()
    print 'Sum: ' + str(number_sum) + '(calculated in ' + str(time.clock() - start) + ')'

main()
