import sys
import time

d = {0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6,100:7,1000:8}

def string_size(n):
    if n < 100:
	if d.has_key(n):
	    return d[n]
	else:
	    return d[(n/10)*10] + d[n%10]
    elif n < 1000:
	x = string_size(n%100)
	if x > 0:
	    return d[n/100] + d[100] + 3 + x
	else:
	    return d[n/100] + d[100] + x
    else:
	return d[n/1000] + d[1000] + string_size(n%1000)

def main():
    start = time.clock()
    try:
	i = 1
	sum_of_characters = 0
	while i <= 1000:
	    sum_of_characters += string_size(i)
	    i += 1

    except KeyboardInterrupt:
        print 'Current sum: ' + str(sum_of_characters) + '(calculated in ' + str(time.clock() - start) + ')'
        sys.exit()
    print 'Sum: ' + str(sum_of_characters) + '(calculated in ' + str(time.clock() - start) + ')'

main()
