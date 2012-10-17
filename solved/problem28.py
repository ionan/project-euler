from time import time

start = time()

def getNthRingCorners(ring):
	prevElem = sum([8*x for x in range(1,ring)])+1
	corners = [prevElem+2*ring,prevElem+4*ring,prevElem+6*ring,prevElem+8*ring]
	return corners

def main(dimension):
	if dimension % 2 == 0:
		print 'Wrong dimension!'
		return
	
	rings = (dimension - 1) / 2
	
	s = 1
	ring = 1
	while ring <= rings:
		s += sum(getNthRingCorners(ring))
		ring += 1

	print 'The sum of diagonals is ' + str(s) + ' (execution took ' + str(time()-start) + ' seconds)'

main(1001)
