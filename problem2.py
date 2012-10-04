import sys
import time

def main():
    start = time.clock()
    sum = 0
    x = 1
    y = 2
    while y < 4000000:
	if y % 2 == 0:
	    sum = sum + y
	lag = x	
	x = y
	y =  lag + x
	

    print 'Sum: ' + str(sum) + '(calculated in ' + str(time.clock() - start) + ')'

main()
