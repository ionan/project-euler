from math import sqrt

def sumOfDivisiors(n):
	s = 1
	candidate = 2
	limit = int(sqrt(n) + 1)
	while candidate < limit:
		if n % candidate == 0:
			s += candidate + (n / candidate)
		candidate += 1
	return s

def main():
	dic = {}
	sumOfAmicables = 0
	for x in range(2,10002):
		s = sumOfDivisiors(x)
		if s > 10000:
			continue
		if s < x:
			if dic.has_key(s) and dic[s] == x:
				sumOfAmicables += s + x
		else:
			dic[x] = s
	print 'Sum of amicable numbers is ' + str(sumOfAmicables)
main()
