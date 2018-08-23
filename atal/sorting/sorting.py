import sys, os
import time
sys.path.append('..')

from algorithms import custom_sort

count = 1
total_time = 0
output = open('output.txt', 'w')

with open('input.txt', 'r') as arquivo:
	for ith_list in arquivo:
		alist = map(int, ith_list.split())
		
		start = time.clock()
		sorted_list = custom_sort(alist)
		finish = time.clock()
		
		str_list = " ".join(str(x) for x in sorted_list)
		
		time_diff = (finish - start) * 1000000
		total_time += time_diff
		
		output.write("Case {}: ".format(count) + str_list + "\n")
		output.write("Took to Execute: {} microseconds\n\n".format(time_diff))
		count += 1

output.close()
print "Total time: {} microseconds".format(total_time)
