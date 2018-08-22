import time

def custom_sort(alist):
	start = time.clock()
	for j in xrange(len(alist)):
		for i in xrange(len(alist)-1):
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
	finish = time.clock()
	
	time_diff = (finish - start)
	print "It took {} seconds to sort the list".format(time_diff)
	print "Check the output file..."
	return alist
