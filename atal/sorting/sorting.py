import sys, os
sys.path.append('..')

from algorithms import custom_sort

with open('input.txt', 'r') as arquivo:
	alist = arquivo.readline()
alist = map(int, alist.split())

sorted_list = custom_sort(alist)
str_list = " ".join(str(x) for x in sorted_list)

output = open('output.txt', 'w')
output.write(str_list)
output.close()
