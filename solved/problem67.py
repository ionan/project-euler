import sys
import time
import shlex
from shlex import split

tree = []

def build_tree():
    f = open('./triangle2.dat', 'r')
    depth = 0
    for line in f:
	numbers = split(line)
	for number in numbers:
	    tree.append(int(number))
	depth += 1
    return depth

def get_triangle_number(n):
    #(1/2)(n+1)n
    return int(0.5 * n * (n + 1))

def get_row(n):
    j = 1
    while True:
	c = get_triangle_number(j)
	if n < c:
	    return j
	j += 1

def main():
    #Uses bottom -> up approach
    start = time.clock()
    depth = build_tree()
    end = get_triangle_number(depth - 1)
    try:
	i = end - 1
    	while i  >= 0:
	    row = get_row(i)
	    tree[i] = tree[i] + max(tree[i + row],tree[i + row + 1])
	    i -= 1
    except KeyboardInterrupt:
	print 'Tree: ' + str(tree) + '(calculated in ' + str(time.clock() - start) + ')'
    print 'Max sum: ' + str(tree[0]) + '(calculated in ' + str(time.clock() - start) + ')'

main()
