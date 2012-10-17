from time import time

start = time()

def main():
	s = set()
	for a in range(2,101):
		for b in range(2,101):
			elem = a**b
			if elem not in s:
				s.add(elem)
	print 'It creates a sequence of ' + str(len(s)) + ' elements (execution took ' + str(time()-start) + ' seconds)'

main()
