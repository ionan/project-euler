import sys
import time

def main():
    start = time.clock()
    square_sum = 0
    total_sum = 0
    for i in xrange(101):
	square_sum = square_sum + pow(i,2)
	total_sum = total_sum + i
    total_sum = pow(total_sum,2)
    print 'Difference: ' + str(total_sum) + ' - ' + str(square_sum) + ' = ' + str(total_sum - square_sum) + ' (calculated in ' + str(time.clock() - start) + ')'

main()
