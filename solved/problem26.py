from time import time

start = time()

def getCycleLength(a,b):
	#a/b
	div = a / b
	rem = a % b
	s = str(div) + "."
	itr = 0
	cycle = {}	 	
	while rem > 0:
		#print '\t' + str(div) + ' and ' + str(rem)
		cycle[str(div) + '#' + str(rem)] = itr 
		div = (rem * 10) / b
		rem = (rem * 10) % b
		key = str(div) + '#' + str(rem)
		if cycle.has_key(key):
			return len(cycle) - cycle[key]
		s += str(div)
		itr += 1
		cycle[key] = itr
	return 0

def main():
	currentD = 1
	cycleLength = 0
	for d in range(1,1000):
		c = getCycleLength(1,d)
		if c > cycleLength:
			cycleLength = c
			currentD = d
	print str(currentD) + ' has a cycle of ' + str(cycleLength) + ' (execution took ' + str(time()-start) + ' seconds)'

main()
