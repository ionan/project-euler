import sys
import time
import math
from math import sqrt

true = 1
false = 0

def is_palindrome(n):
    if reverse(n) == n:
	return true
    else:
	return false

def reverse(n):
    reverse_n = 0
    lag = n
    while lag > 0:
	reverse_n = reverse_n * 10 + lag % 10
	lag = lag / 10
    return reverse_n

def bigger_factors(x,y,factor_1,factor_2):
    if (x > factor_1 or x > factor_2) or (y > factor_1 or y > factor_2):
	return true
    else:
	return false

def main():
    largest_palindrome = 0
    factor_1 = 0
    factor_2 = 0
    start = time.clock()
    for x in reversed(range(100,999)):
	for y in reversed(range(100,999)):
	    if bigger_factors(x,y,factor_1,factor_2):
		if is_palindrome(x*y) and x*y > largest_palindrome:
		    print 'Palindrome found: ' + str(x * y) + '(' + str(x) + '*' + str(y) +')'
		    largest_palindrome = x * y
		    factor_1 = x
		    factor_2 = y
	    else:
		break
    print 'Largest palindrome number(' + str(factor_1) + '*' + str(factor_2) +'): ' + str(largest_palindrome) + '(calculated in ' + str(time.clock() - start) + ')'

main()
