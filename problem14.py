import sys
import time

def get_next_element(i):
    if i % 2 == 0:
	return i / 2
    else:
	return 3 * i + 1   

def main():
    start = time.clock()
    start_number = 1
    chain_sequence = 1
    i = 2
    try:
	while i < 1000000:
	    hlp = get_next_element(i)
	    current_chain_sequence = 2
	    while hlp != 1:
		hlp = get_next_element(hlp) 
		current_chain_sequence += 1
	    if current_chain_sequence > chain_sequence:
		chain_sequence = current_chain_sequence
		start_number = i
	    i += 1

    except KeyboardInterrupt:
        print 'Current start number: ' + str(start_number) + '(calculated in ' + str(time.clock() - start) + ')'
        sys.exit()
    print 'Start number: ' + str(start_number) + '(calculated in ' + str(time.clock() - start) + ')'

main()
