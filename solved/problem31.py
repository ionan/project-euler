from time import time

start = time()

def loop(amount, coins):
	if len(coins) == 0 or amount < 0:
		return 0
	if amount == 0:
		return 1
	return loop(amount - coins[0],coins) + loop(amount,coins[1:])

def main():
	coins = [1,2,5,10,20,50,100,200]
	c = loop(200,coins)
	print 'There are ' + str(c) + ' ways (execution took ' + str(time()-start) + ' seconds)'

main()
