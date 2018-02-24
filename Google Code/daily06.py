# % operator
# The % operator takes a printf-type format string on the left (%d int, %s string, %f/%g floating point), and the matching values in a tuple on the right (a tuple is made of values separated by commas, typically grouped inside parentheses)
text = "%d little pigs come out or I'll %s and %s and %s" % (3, 'huff', 'puff', 'blow down')
print(text)


# add parens to make the long-line work:
text2 = ("%d little pigs come out or I'll %s and %s and %s" % 
	(3, 'huff', 'puff', 'blow down'))
print(text2)



text3 = 'this is not that bad at all'
first = text3.find('not')
second = text3.find('bad')
result1 = text3[0:first]
result2 = text3[second+3:]
result = result1 +'good' + result2
print(first, second)
print(result)

i = 3
print(i//2)

words = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
words2 = sorted(words)
print(words2)