import sys

scoreTable = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,
			  'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,
			  'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

arr = []

sys.setrecursionlimit(1500)

def swap(idx1,idx2):
	global arr
	x = arr[idx1]
	arr[idx1] = arr[idx2]
	arr[idx2] = x

def partition(left,right):
	global arr
	pivot = (right+left)/2
	swap(pivot,left)
	pivot = left
	limit = left+1
	for idx in range(left + 1,right):
		if arr[pivot] > arr[idx]:
			swap(idx,limit)
			limit += 1
	swap(pivot,limit-1)
	pivot = limit-1
	return pivot

def quickSort(left,right):
	global arr
	if left >= right:
		return
	pivot = partition(left,right)
	quickSort(left,pivot)
	quickSort(pivot+1,right)

def getScore(word):
	score = 0
	for char in word.upper():
		score += scoreTable[char]
	return score

def readFile():
	global arr
	f = open('names.txt','r')
	arr = f.read().replace('"','').replace('\n','').split(',')

def main():
	readFile()
	#arr = sorted(arr)
	quickSort(0,len(arr))
	totalScore = 0
	for wordIdx in range(0,len(arr)):
		totalScore += (wordIdx + 1) * getScore(arr[wordIdx])
	print 'The sum of all scores is ' + str(totalScore)

main()
