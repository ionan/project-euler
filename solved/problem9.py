import sys
import time

def main():
    start = time.clock()
    a = 0
    b = 0
    c = 0
    for a in xrange(0,1000):
        for b in xrange(a + 1,1000):
            c = 1000 - a - b
            if c > b and a**2 + b**2 == c**2:
                print 'Pythagorean triplet: a = ' + str(a) + ', b = ' + str(b)  + ', c = ' + str(c) + '(calculated in ' + str(time.clock() - start) + ')'
                print 'Pythagorean triplet\'s product: ' + str(a*b*c) 
                exit()
    print 'Pythagorean triplet not found!! (running time: ' + str(time.clock() - start) + ')'
        

main()
