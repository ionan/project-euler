import sys
import time

def main():
    start = time.clock()
    number = pow(2,1000)
    sum_of_digits = 0
    try:
	while number != 0:
	    sum_of_digits = sum_of_digits + number % 10
	    number = number / 10

    except KeyboardInterrupt:
        print 'Current sum: ' + str(sum_of_digits) + '(calculated in ' + str(time.clock() - start) + ')'
        sys.exit()
    print 'Sum: ' + str(sum_of_digits) + '(calculated in ' + str(time.clock() - start) + ')'

main()
