import time

start = time.time()

def main():
	n1 = 1
	n2 = 1
	f = 0
	i = 3
	while True:
		f = n1+n2
		n2 = n1
		n1 = f
		if len(str(f)) >= 1000:
			break
		i += 1
	print 'The first element is F' + str(i) + '=' + str(f) + ' (execution took ' + str(time.time()-start) + ' seconds)'

main()
