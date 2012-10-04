import sys
import time

def get_number_of_divisors(n):
    #Divisor function
    number_of_divisors = 1
    if n == 1:
        return number_of_divisors
    hlp = 1
    #By 2??
    while n % 2 == 0:
        n /= 2
        hlp += 1
    #Update number of divisors
    number_of_divisors *= hlp
    if n == 1:
        return number_of_divisors
    hlp = 1
    #By 3??
    while n % 3 == 0:
        n /= 3
        hlp += 1
    #Update number of divisors
    number_of_divisors *= hlp
    if n == 1:
        return number_of_divisors
    #By 6k +1???
    k = 1
    while True:
        hlp = 1
        current = 6 * k - 1
        while n % current == 0:
            n /= current
            hlp += 1
        number_of_divisors *= hlp
        if n == 1:
            return number_of_divisors
        hlp = 1
        current = 6 * k + 1
        while n % current == 0:
            n /= current
            hlp += 1
        number_of_divisors *= hlp
        if n == 1:
            return number_of_divisors
        k += 1

def get_triangle_number(n):
    #(1/2)(n+1)n
    return 0.5 * n * (n + 1)

def main():
    start = time.clock()
    candidate = -1
    divisors = -1
    try:
	number = 1
        while True:
            triangle = get_triangle_number(number)
            divisors = get_number_of_divisors(triangle)
            if divisors >= 500:
     	        upper_bound = triangle
		candidate = triangle
		break
	    number += 1

    except KeyboardInterrupt:
        print 'Factor range: ' + str(divisors) + ', current number: ' + str(triangle) + ', candidate: ' + str(candidate) + '(calculated in ' + str(time.clock() - start) + ')'
        sys.exit()
    print 'First number: ' + str(candidate) + '(calculated in ' + str(time.clock() - start) + ')'

main()
