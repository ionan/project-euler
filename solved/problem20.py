def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)

def main():
	f = fact(100)
	s = 0
	while f/10 != 0:
		s += f%10
		f = f/10
	s += f
	print 'The sum is ' + str(s)

main()
