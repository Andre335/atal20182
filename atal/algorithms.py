import time

# Sort with O(n^2) complexity
def custom_sort(alist):
	start = time.clock()
	for j in xrange(len(alist)):
		for i in xrange(len(alist)-1):
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
	finish = time.clock()
	
	time_diff = (finish - start) * 1000000
	print "It took {} microseconds to sort the list".format(time_diff)
	print "Check the output file to see the result..."
	return alist
