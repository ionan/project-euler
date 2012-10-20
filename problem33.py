from time import time

start = time()

def isNonTrivialFraction(num,den):
	division = float(num)/float(den)
	try:
		if num == den:
			return False
		if str(num)[0] == str(den)[1]:
			return float(str(num)[1])/float(str(den)[0]) == division
		if str(num)[1] == str(den)[0]:
			return float(str(num)[0])/float(str(den)[1]) == division
		return False
	except IndexError:
		print '\t' + str(num) + ' and ' + str(den)
		return False
	except ZeroDivisionError:
		return False

def multiplyFractions(fractionArray):
	print fractionArray
	num = 1
	den = 1
	for x in fractionArray:
		num *= int(x[:x.find('/')])
		den *= int(x[x.find('/')+1:])
	print str(num) + '/' + str(den)

def main():
	nonTrivialFractions = []
	for x in range(10,99):
		for y in range(x,99):
		#
			num = x
			den = y
			if isNonTrivialFraction(num,den):
				nonTrivialFractions.append(str(num) + '/' + str(den))
		#
		#num = den
		#den = x
		#if isNonTrivialFraction(num,den):
		#	nonTrivialFractions.append(str(num) + '/' + str(den))
	multiplyFractions(nonTrivialFractions)

main()
