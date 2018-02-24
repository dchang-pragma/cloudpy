def function_read(file_name):
	"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""
	mimic_dict = {}
	f = open(file_name, 'rU')
	text = f.read()
	#processed_string = text.rstrip('\n')
	processed_string = text.strip('\n').replace("\n", "")
	#processed_string = text.splitlines()
	f.close()
	word_list = processed_string.split(' ')
	# for line in f:   ## iterates over the lines of the file
	#     #print(line.rstrip())    ## trailing , so print does not add an end-of-line char
	#     #print(type(line)) # string type
	#     line_count = line_count + 1
	#     line_string = line.rstrip('\n').lower()
	#     word_list = line_string.split(' ')
	#     #print(word_list)
	#     for word in word_list:
	#     	if word not in word_count.keys():
	#     		word_count[word] = 1
	#     	else:
	#     		word_count[word] = word_count[word] + 1
	#print (word_count)
	#print(text, type(text))
	#print(processed_string, type(processed_string))
	print(word_list)



	               ## since 'line' already includes the end-of line.
	
	return mimic_dict
	#print(line_count)

def get_count(word_count_tuple):
  """Returns the count from a dict word/count tuple  -- used for custom sort."""
  return word_count_tuple[1]



word_summary = function_read('small.txt')
# for k, v in word_summary.items():
# 	print (k,'  ',v)

# words_sorted = sorted(word_summary.keys())
# for word in words_sorted:
# 	print(word, word_summary[word])

# word_summary_top = sorted(word_summary.items(), key=get_count, reverse = True) # from dict to sorted list

# print(type(word_summary_top))
# for item in word_summary_top:
# 	print(item[0], item[1])
# #print(word_summary)