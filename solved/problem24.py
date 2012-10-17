import time

start = time.time()

def fact(n):
	if n < 2:
		return 1
	return n * fact(n-1)

def createPermutation(st,elems):
	for i in elems:
		st += str(i)
	return st

def main(elems,nthPerm):
	limit = len(elems)
	if fact(limit) < nthPerm:
		return None #It is not possible to get such permutation
	nthPerm -= 1
	elems = sorted(elems)
	nthLexPerm = ''
	for x in range(0,limit):
		f = fact(limit-1-x)
		idx = nthPerm/f
		nthLexPerm = nthLexPerm + str(elems[idx])
		elems.pop(idx)
		nthPerm = nthPerm % f
		if nthPerm ==  0:
			return createPermutation(nthLexPerm,elems)

print 'The 1.000.000th permutation is ' + main([0,1,2,3,4,5,6,7,8,9],1000000) + ' (execution took ' + str(time.time()-start) + ' seconds)'
