import random

VALUES_SIZE = 1000
WEIGHTS_SIZE = 100
NUM_OF_LISTS = 100
SMALL_INPUT_SIZE = 15
MEDIUM_INPUT_SIZE = 20
BIG_INPUT_SIZE = 30

count = 0
output_file = open('small.txt', 'w')
for i in xrange(NUM_OF_LISTS):
	outputt = []
	weights = []
	values = []
	for j in xrange(SMALL_INPUT_SIZE):
		weights.append(int(random.random() * WEIGHTS_SIZE))
		values.append(int(random.random() * VALUES_SIZE))
	outputt.append(weights)
	output_str = " ".join(str(x) for x in outputt)
	output_file.write(output_str + "\n")
	
	outputt = []
	outputt.append(values)
	output_str = " ".join(str(x) for x in outputt)
	output_file.write(output_str + "\n")
	count += 1
output_file.close()
print "Adicionadas {} listas small.".format(count)

count = 0
output_file = open('medium.txt', 'w')
for i in xrange(NUM_OF_LISTS):
	outputt = []
	weights = []
	values = []
	for j in xrange(MEDIUM_INPUT_SIZE):
		weights.append(int(random.random() * WEIGHTS_SIZE))
		values.append(int(random.random() * VALUES_SIZE))
	outputt.append(weights)
	output_str = " ".join(str(x) for x in outputt)
	output_file.write(output_str + "\n")
	
	outputt = []
	outputt.append(values)
	output_str = " ".join(str(x) for x in outputt)
	output_file.write(output_str + "\n")
	count += 1
output_file.close()
print "Adicionadas {} listas medium.".format(count)

count = 0
output_file = open('big.txt', 'w')
for i in xrange(NUM_OF_LISTS):
	outputt = []
	weights = []
	values = []
	for j in xrange(BIG_INPUT_SIZE):
		weights.append(int(random.random() * WEIGHTS_SIZE))
		values.append(int(random.random() * VALUES_SIZE))
	outputt.append(weights)
	output_str = " ".join(str(x) for x in outputt)
	output_file.write(output_str + "\n")
	
	outputt = []
	outputt.append(values)
	output_str = " ".join(str(x) for x in outputt)
	output_file.write(output_str + "\n")
	count += 1
output_file.close()
print "Adicionadas {} listas big.".format(count)
