hash = {}
hash['word'] = 'garfield'
hash['count'] = 42
s = 'I want %(count)d copies of %(word)s' %hash  # %d for int, %s for string
# 'I want 42 copies of garfield'
print(hash)


dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'

#print(dict)  ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

#print(dict['a'])     ## Simple lookup, returns 'alpha'
dict['a'] = 6       ## Put new key/value into dict
'a' in dict         ## True
## print dict['z']                  ## Throws KeyError
if 'z' in dict:
	print(dict['z'])     ## Avoid KeyError
print(dict['o'])
print(dict.get('z','not found'))  ## None (instead of KeyError)
print(dict)
print(dict.keys())
print(dict.items())

if 'a' in dict:
	print('yes')
