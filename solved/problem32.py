from time import time

start = time()

oneToNine = [x for x in range(1,10)]

def isPandigital(multcnd,multplr,product):
	numbers = list(str(multcnd) + str(multplr) + str(product))
	numbers.sort()
	length = len(numbers)
	if length != 9:
		return False
	#numberSet = set(char for char in numbers)

	for x in range(0,length):
		if int(numbers[x]) != int(oneToNine[x]):
			return False

	#Check if all numbers are represented
	#if len(oneToNine.intersection(numberSet)) > 0:
	#	return False
	return True

def main():
	pandigitalNumbers = set()
	#for x in range(1,98765432):
	#	for y in range(1,98765432):
	for x in range(1,98):
		for y in range(123,9876):
			#if x*y > 1000000:
			#	break
			if isPandigital(x,y,x*y):
				pandigitalNumbers.add(x*y)
	print 'Sum of ' + str(len(pandigitalNumbers)) + ' pandigital numbers found is ' + str(sum(pandigitalNumbers)) + ' (execution took ' + str(time()-start) + ' seconds)'

#print isPandigital(163,257,498) # True
#print isPandigital(16,257,498) # False
#print isPandigital(1663,257,498) # False
#print isPandigital(163,257,4938) # False
#print isPandigital(39,186,7254) # True

#Wiser approach:
#		1	2	3	4	5	6	7	8	9
#	1   #   #   #  [9]  #   #   #   #   #
#	2   #   #  [9]  #   #   #   #   #   #
#	3   #  [9]  #   #   #   #   #   #   #
#	4  [9]  #   #   #   #   #   #   #   #
#	5   #   #   #   #   #   #   #   #   #
#	6   #   #   #   #   #   #   #   #   #
#	7   #   #   #   #   #   #   #   #   #
#	8   #   #   #   #   #   #   #   #   #
#	9   #   #   #   #   #   #   #   #   #

main()
