def function_open(file_name):
	line_count = 0
	word_count = {}
	f = open(file_name, 'rU')
	for line in f:   ## iterates over the lines of the file
	    #print(line.rstrip())    ## trailing , so print does not add an end-of-line char
	    #print(type(line)) # string type
	    line_count = line_count + 1
	    line_string = line.rstrip('\n').lower()
	    word_list = line_string.split(' ')
	    #print(word_list)
	    for word in word_list:
	    	if word not in word_count.keys():
	    		word_count[word] = 1
	    	else:
	    		word_count[word] = word_count[word] + 1
	#print (word_count)



	               ## since 'line' already includes the end-of line.
	f.close()
	return word_count
	#print(line_count)

def get_count(word_count_tuple):
  """Returns the count from a dict word/count tuple  -- used for custom sort."""
  return word_count_tuple[1]


#function_open('alice.txt')
word_summary = function_open('alice.txt')
# for k, v in word_summary.items():
# 	print(k,' ',v)
#word_summary_sorted = sorted(word_summary.keys())
word_summary_sorted = sorted(word_summary.items(), key=get_count, reverse=True)


# for item in word_summary_sorted[:20]:
# 	print(item[0], item[1])
# print(type(word_summary_sorted))

outf = open('test_output.txt', 'w')
outf.write('text' + '\n')
outf.close()


