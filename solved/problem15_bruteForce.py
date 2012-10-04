import sys
import time

dimX = 10
dimY = 10

def is_valid_route(n):
    n = int(n[2:])
    X_steps = 0
    Y_steps = 0
    index = 1
    while index <= (dimX + dimY):
	hlp = n % 10
	if hlp == 0:
	    X_steps += 1
	elif hlp == 1:
	    Y_steps += 1
	else:
	    return False
	n = n / 10
	index += 1
    if X_steps == dimX and Y_steps == dimY:
	return True
    else:
	return False

def bin_to_int(b):
    i = int(b[2:])
    end = len(b) - 2
    number = 0
    index = 0
    while index <= end:
	number += (i % 10) * pow(2,index)
	i /= 10
    	index += 1
    return number

def fixed_size_bin(b,size):
    h = bin(b)[2:]
    return '0b' + (size + len(h[2:])) * '0' + h 

def main():
    start = time.clock()
    max_number = '0b' + dimY * '1' + (dimX - 1) * '0' + '1'
    start_number = '0b' + dimX * '0' + dimY * '1'
    print 'Numbers from ' + str(bin_to_int(start_number)) + ' to ' + str(bin_to_int(max_number))  
    number_of_routes = 0
    try:
	i = bin_to_int(start_number)
	end = bin_to_int(max_number)
	while i <= end:
	    if is_valid_route(fixed_size_bin(i, dimX + dimY)):
		number_of_routes += 1
		#print 'Valid route: ' + str(fixed_size_bin(i, dimX + dimY))
	    i += 1
    except KeyboardInterrupt:
        print 'Current number of routes: ' + str(number_of_routes) + ', iterations left: ' + str(end - i) + '(calculated in ' + str(time.clock() - start) + ')'
        sys.exit()
    print 'Number of routes: ' + str(number_of_routes) + '(calculated in ' + str(time.clock() - start) + ')'

main()
