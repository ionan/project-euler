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
	elems = sorted(elems)
	nthLexPerm = ''
	for x in range(0,limit):
		f = fact(limit-1-x)
		idx = f/nthPerm
		print str(f) + ' / ' + str(nthPerm) + ' is ' + str(idx)
		if idx > limit:
			return None #It is not possible to get such permutation
		#elif idx == 0:
		#	
		#	return createPermutation(nthLexPerm,elems)
		else:
			nthLexPerm = nthLexPerm + str(elems[idx])
			if idx > 0:
				elems = elems[:idx-1] + elems[idx:]
			else:
				elems = elems[idx:]
			print elems			
			nthPerm = f % nthPerm
			print nthPerm
		if nthPerm ==  0:
			return createPermutation(nthLexPerm,elems)

print main([0,1,2],3)
