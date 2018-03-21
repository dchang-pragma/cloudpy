# initialize a list
result = [None] * 5
result[1] = 5
print(result)



nums = [1, 2, 3, 4]

squares = [ n * n for n in nums ]
#print(squares)

strs = ['hello', 'and', 'goodbye']

shouting = [ s.upper() + '!!!' for s in strs ]
#print(shouting)


## Select values <= 2
nums = [2, 8, 1, 6]
small = [ n for n in nums if n <= 2 ]  ## [2, 1]
#print(small)

## Select fruits containing 'a', change to upper case
fruits = ['apple', 'cherry', 'bannana', 'lemon']
afruits = [ s.upper() for s in fruits if 'a' in s ]
#print(afruits)
## ['APPLE', 'BANNANA']








