import sys, os
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('file', metavar='file_name', type=str, nargs='+')
args = parser.parse_args()
file_name = args.file[0] + ".txt"

sys.path.append('..')

from algorithms import mochila_binaria

count = 1
total_time = 0
output = open('output.txt', 'w')
two = 0
with open(file_name, 'r') as arquivo:
	for ith_list in arquivo:
		ith_list = ith_list.replace(",", "")
		ith_list = ith_list.replace("[", "")
		ith_list = ith_list.replace("]", "")
		
		alist = map(int, ith_list.split())
		if two == 0: 
			weights = alist
			two += 1
		elif two == 1: 
			values = alist
			two += 1
		
		if two == 2:
			start = time.clock()
			max_value = mochila_binaria(5000, weights, values, len(values))
			finish = time.clock()
			
			time_diff = (finish - start)
			total_time += time_diff
			
			output.write("Caso {}: ".format(count) + str(max_value) + "\n")
			output.write("Executou em: {} segundos\n\n".format(time_diff))
			count += 1
			two = 0

output.close()
print "Tempo total: {} segundos".format(total_time)
