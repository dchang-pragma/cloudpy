import re
str = 'an example word:cat!!'
match0 = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
# r: raw string
if match0:                      
    print('found', match0.group()) ## 'found word:cat'
else:
    print('did not find')



## Search for pattern 'iii' in string 'piiig'.
## All of the pattern must match, but it may appear anywhere.
## On success, match.group() is matched text.
match1 = re.search(r'iii', 'piiig')
if match1:
	print(match1.group())
	print(type(match1))

match2 = re.search(r'igs', 'piiig') # no match
if match2:
	print(match2.group())

# ## . = any char but \n
match3 = re.search(r'..g', 'piiig') #found, match.group() == "iig"

# ## \d = digit char, \w = word char
match4 = re.search(r'\d\d\d', 'p123g') # found, match.group() == "123"
match5 = re.search(r'\w\w\w', '@@abcd!!') # found, match.group() == "abc"
match6 = re.search(r'\W\W', '@@abcd!!') 


if match6:
	print('match6', match6.group())

 ## i+ = one or more i's, as many as possible.
match7 = re.search(r'pi+', 'piiig') # found, match.group() == "piii"

## Finds the first/leftmost solution, and within it drives the +
## as far as possible (aka 'leftmost and largest').
## In this example, note that it does not get to the second set of i's.
match8 = re.search(r'i+', 'piigiiii') # found, match.group() == "ii"

## \s* = zero or more whitespace chars
## Here look for 3 digits, possibly separated by whitespace.
match9 = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx') #  found, match.group() == "1 2   3"
match10 = re.search(r'\d\s*\d\s*\d', 'xx12  3xx') #  found, match.group() == "12  3"
match11 = re.search(r'\d\s*\d\s*\d', 'xx123xx') # found, match.group() == "123"

## ^ = matches the start of string, so this fails:
match12 = re.search(r'^b\w+', 'foobar') #  not found, match == None
## but without the ^ it succeeds:
match13 = re.search(r'b\w+', 'foobar') # found, match.group() == "bar"


email_str = 'purple alice-b@google.com monkey dishwasher'


match14 = re.search(r'\w+@\w+', email_str)
match15 = re.search(r'[\w.-]+@[\w.-]+', email_str)
match16 = re.search(r'[\w-]+@[\w.]+', email_str)


print(match16.group())

match17 = re.search('([\w.-]+)@([\w.-]+)', email_str)
if match17:
    print(match17.group())   ## 'alice-b@google.com' (the whole match)
    print(match17.group(1))  ## 'alice-b' (the username, group 1)
    print(match17.group(2))  ## 'google.com' (the host, group 2)

    # Open file
f = open('small.txt', 'r')
# Feed the file text into findall(); it returns a list of all the found strings
strings = re.findall(r'we', f.read())
print(strings,type(strings))
f.close()




#greedy_nongreedy
gn_str1 = '<b>foo</b>'
gn_str2 = '<i>so on</i>'
match17 = re.search('<.*>', gn_str1) #greedy; * goes as far as is it can
match18 = re.search('<.*?>', gn_str1) #non_greedy
print(match17.group())
print(match18.group())
