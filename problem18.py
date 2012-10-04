import sys
import time
import shlex
from shlex import split

tree = []

def build_tree():
    f = open('./triangle.dat', 'r')
    depth = 0
    for line in f:
	numbers = split(line)
	for number in numbers:
	    tree.append(int(number))
	depth += 1
    return depth

def get_max_sum(my_pos, left, my_row):
    try:
    	if left == 0:
	    return 0
    	else:
	    left_sum = get_max_sum(int(my_pos + my_row), left - 1, my_row + 1)
	    right_sum = get_max_sum(int(my_pos + my_row) + 1, left - 1, my_row + 1)
    	    return tree[my_pos] + max(left_sum,right_sum)
    except TypeError:
	print 'Wrong index: ' + str(my_pos)

def main():
    start = time.clock()
    depth = build_tree()
    left_sum = get_max_sum(1, depth - 1, 2)
    right_sum = get_max_sum(2, depth - 1, 2)
    max_sum = tree[0] + max(left_sum,right_sum) 	
    print 'Max sum: ' + str(max_sum) + '(calculated in ' + str(time.clock() - start) + ')'

main()
