import codecs

f = codecs.open('small.txt', 'rU', 'utf-8')
for line in f:
	print(line)
  # here line is a *unicode* string
f.close()