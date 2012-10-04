import sys
import time

true = 1
false = 0

def is_divisible(n):
    #Is divisible by numbers from 1 to 20 = is divisible by 20,19,18,17,16,15,14,13,12,11
    if n % 20 == n % 19 == n % 18 == n % 17 == n % 16 == n % 15 == n % 14 == n % 13 == n % 12 == n % 11 == 0:
	return true
    else: 	
	return false

def main():
    start = time.clock()
    smallest_number = 0
    i = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
    while 1:
	if is_divisible(i):
	    smallest_number = i
	    break
	i = i + 1

    try:
        assert is_divisible(smallest_number)
    except AssertionError: 
	print 'Erro when asserting condition!!! (' + str(time.clock() - start) + ' elapsed)' 
	sys.exit()

    print 'Smallest number: ' + str(smallest_number) + '(calculated in ' + str(time.clock() - start) + ')'

main()
