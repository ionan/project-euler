import time

start = time.time()

def permute(elems):
	elems.sort(reverse=True)
	if len(elems) == 1:
		return elems
	else:
		total = []
		for idx,val in enumerate(elems):
			total += [str(val) + str(c) for c in permute([x for i,x in enumerate(elems) if i != idx])]
		return total
		
def is_pandigital(numb):
	result = [False,-1,[],""]
	for i in range(1,9):
		test = int(numb[0:i])
		subnumb = numb[i:]
		muli = 2
		while len(subnumb) > 0:
			t = test * muli
			if subnumb.find(str(t)) == 0:
				muli += 1
				subnumb = subnumb[len(str(t)):]
			else:
				break
		if len(subnumb) == 0:
			result = [True,test,range(1,muli),numb]
			break
	return result
	
def main():
	candidates = permute([1,2,3,4,5,6,7,8,9])
	for candidate in candidates:
		result = is_pandigital(candidate)
		if result[0]:
			print result
			print 'Execution took ' + str(time.time()-start) + ' seconds'
			break

main()
