var = 6
del var  # var no more!

list = ['a', 'b', 'c', 'd']
#del list[0]     ## Delete first element
list.remove('a')
del list[-2:]   ## Delete last two elements
print(list)      ## ['b']

dict = {'a':1, 'b':2, 'c':3}
del dict['b']   ## Delete 'b' entry
print(dict)      ## {'a':1, 'c':3}