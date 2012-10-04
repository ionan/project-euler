import sys
import time

def main():
    start = time.clock()
    sum = 0
    i = 5
    while i < 1000:
	if i % 3 != 0:
	    sum = sum + i
	i = i + 5

    i = 3
    while i < 1000:
	sum = sum + i
	i = i + 3
	
    print 'Sum: ' + str(sum) + '(calculated in ' + str(time.clock() - start) + ')'

main()


