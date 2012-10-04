import sys
import time
import math
from math import sqrt

def is_prime(n):
    #'Naive' method: check wether 2 to sqrt(n) are factors or not
    max = int(sqrt(n))
    i = 2
    while i <= max:
        if n % i == 0:
            return False
        i = i + 1
    return True
    
def main():
    start = time.clock()
    prime_number = 1
    i = 3
    while True:
        if is_prime(i):
            prime_number = prime_number + 1
        if prime_number == 10001:
            print '10001st prime number: ' + str(i) + '(calculated in ' + str(time.clock() - start) + ')'
            exit()
        #Skip even numbers
        i = i + 2

main()
